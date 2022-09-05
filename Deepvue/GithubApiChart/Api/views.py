from datetime import datetime
import json
from ast import literal_eval
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response("Visit the Api end point /repos with payload to get response of top 10 repos of the org")

@api_view(['POST'])
def repos(request):

    print(request)
    stime = datetime.now()
    try:
        org = request.data.get("org")
        top = request.data.get("top")
    except:
        request = json.loads(request.body.decode('utf-8'))
        print(request)
        org = request['org']
        top = request['top']

    header = {
        "Accept": "application/vnd.github+json",
        # "Authorization": f"Bearer {gh_tokken}"
    }
    
    url = f'https://api.github.com/orgs/{org}/repos?per_page=50&page=1'

    response = requests.get(url, headers=header)
    print(response.headers)

    ttbor = response.elapsed.total_seconds() # Time Takken By one Request
    ttbar = ttbor # Time takken By all request (will be added one By one)

    n = 0
    if "Link" in response.headers:
        # Calculating Number of pages (due to pagination) to reach
        n = int(response.headers["Link"].split(',')[1].split('?')[1].split('&')[-1].split('=')[1].split('>')[0])
    
    result = {}

    if n:
        # Looping Over Pages 
        for i in range(1,n+1):
            url = f'https://api.github.com/orgs/{org}/repos?per_page=50&page={i}'
            response = requests.get(url, headers=header)
            data = json.loads(response.content)
            for d in data:
                print(d['name'], " = ", d['stargazers_count'])
                result[d['name']] = d['stargazers_count']
            ttbar += response.elapsed.total_seconds()
    else:
        data = json.loads(response.content)
        for d in data:
            print(d['name'], " = ", d['stargazers_count'])
            result[d['name']] = d['stargazers_count']

    # Sorting Results According to Stars 
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    final = {
        'results': []
    }

    # Adding Result to final Response 
    if top:
        for i in range(top):
            final['results'].append({
                'name': result[i][0],
                'stars': result[i][1]
            })
    elif len(result) > 10:
        for i in range(10):
            final['results'].append({
                'name': result[i][0],
                'stars': result[i][1]
            })
    else:
        for v in result:
            final['results'].append({
                'name': v[0],
                'stars': v[1]
            })

    etime = datetime.now()
    ttime =  (etime.minute - stime.minute)*60 + etime.second - stime.second

    # Adding Response times 
    final['rps_1'] = ttbor
    final['rps_all'] = ttbar
    final['total_rps'] = ttime

    print("Time Takken By One Request (in seconds)", round(ttbor,3))
    print("Time Takken By All Request combined (in seconds)", round(ttbar, 3))
    return Response(final)
    
@api_view(['POST'])
def commits(request, org, repo):

    print(request)
    stime = datetime.now()

    try:
        since = request.data.get("since")
        until = request.data.get("until")
        view = request.data.get("view")
    except:
        request = json.loads(request.body.decode('utf-8'))
        print(request)
        since = request['since']
        until = request['until']
        view = request['view']

    # Getting view which metrices to save in result (montly, yearly, daily)
    try:
        if view == 'y':
            ymd = 4
        elif view == 'd':
            ymd = 10
        else:
            ymd = 7        
    except:
        ymd = 7

    header = {
        "Accept": "application/vnd.github+json",
        # "Authorization": f"Bearer {gh_tokken}"
    }
    
    url = f"https://api.github.com/repos/{org}/{repo}/commits?since={since}&until={until}&per_page=50&page=1"

    response = requests.get(url, headers=header)
    print(response.headers)

    ttbor = response.elapsed.total_seconds()
    ttbar = ttbor

    n = 0
    if "Link" in response.headers:
        # Getting Number of pages until final response 
        n = int(response.headers["Link"].split(',')[1].split('?')[1].split('&')[-1].split('=')[1].split('>')[0])
    
    result = {}

    if n:
        # Looping over Pages to Get all responses 
        for i in range(1,n+1):
            url = f"https://api.github.com/repos/{org}/{repo}/commits?since={since}&until={until}&per_page=50&page={i}"
            response = requests.get(url, headers=header)
            data = json.loads(response.content)
            for d in data:
                if d['commit']['committer']['date'][:ymd] in result:
                    result[d['commit']['committer']['date'][:ymd]] += 1
                else:
                    result[d['commit']['committer']['date'][:ymd]] = 1
                print(d['commit']['committer']['date'][:ymd]," = ", result[d['commit']['committer']['date'][:ymd]])
            ttbar += response.elapsed.total_seconds()
    else:
        data = json.loads(response.content)
        for d in data:
            if d['commit']['committer']['date'][:ymd] in result:
                result[d['commit']['committer']['date'][:ymd]] += 1
            else:
                result[d['commit']['committer']['date'][:ymd]] = 1

    etime = datetime.now()
    ttime =  (etime.minute - stime.minute)*60 + etime.second - stime.second

    final = {
        'results': [],
        'rps_1': ttbor,
        'rps_all': ttbar,
        'total_rps': ttime
    }
    
    # Adding result to final Response 
    for k,v in result.items():
        final['results'].append({
            'date': k,
            'commits': v
        })

    print("Time Takken By One Request (in seconds)", round(ttbor,3))
    print("Time Takken By All Request combined (in seconds)", round(ttbar, 3))
    return Response(final)
