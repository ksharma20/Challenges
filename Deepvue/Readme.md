# ProgrammingChallenge 
This is to help us understand your programming style and expertise. Getting Started :

For this round, you have to write a simple API server, which fetches data from Github and serializes it in a certain format, and visualizes it in form of charts. 

### It involves a few steps: 
1. Creating a simple back-end API for which you need to make a REST API call to Github's API service and fetch the data 
1. Creating a small front-end application on Django/FastAPI 

**Challenge Duration** - 3 days 

## Backend API 

You will need to write a simple API that returns the top 10 repositories of an organization in Github by stars.

### API Details 
We will send a POST request to your API at /repos with JSON payload containing Github organization name 

For deepvue-tech, this will look like this:
```json
{ 
"org": "deepvue-tech" 
}
``` 
and the API should return a response in the following format (JSON): 
```json
{ 
"results": [ 
{"name":"rick", "stars": 100}, 
{"name":"morty", "stars": 98}, 
{"name":"jerry", "stars":2}, 
] 
}
```
### Metrics 
**Response Time**: Share your findings on response time and the code that you use for the same. 


## Front-End App 

You will need to create a simple Django/FastAPI app with a single view /dashboard having two charts:
- A Bar Chart showing the results of your API i.e Input an organization, plot the top 10 repos and their star counts coming from your end-point. 
- A Line chart showing commits timelines i.e. Input an organization & a repository and select a time range from the time range filter, plot daily total commit during a time range.

## Extras 
3. It is okay to Google or Bing (if that's your thing) 
3. Think through the edge cases, especially for organizations with a large number of repos 
3. Write good, useful docstrings and comments

## Bonus 
4. Add interactivity in graphs/charts to analyze the data coming from APIs 
4. Deploy this as a microservice on a cloud and share the link Submission 
4. Once you are done, email us the solution and findings/notes/logs in a zip file titled <your-name>-fullstack-intern-hiring-challenge.zip

# Solution

### Front-end

#### Dashboard
![image](https://user-images.githubusercontent.com/72795959/188384265-e5fa8c08-a9fe-45f4-ba89-8474a02e6890.png)

After Clicking One of the button, Corresponding form shows up for input 
![image](https://user-images.githubusercontent.com/72795959/188385292-2b246198-35da-48d4-9694-3f6b6dc54d42.png)

After Clicking on Display Button - Form data is sent to JS where request is made and sent to Api Endpoint, Meanwhile Loading screen Comes up !
![image](https://user-images.githubusercontent.com/72795959/188396072-855552d9-02f9-44b6-8a75-6ab36c03779e.png)

After Recieving Response from API endpoint, Data is send to Charts (using chartsjs lib), And then Chart is displayed into a <_canvas_>
![image](https://user-images.githubusercontent.com/72795959/188396835-8ee7c6b0-3d0a-4bcb-aea3-ce0d076eeb41.png)

#### Same Goes for Line Chart
![image](https://user-images.githubusercontent.com/72795959/188397166-3f54857c-664c-4c08-a5b9-abda24c6b125.png)

As view was selected to daily, Therefore, x-axis conatins Dates i.e, 2022-09-03 ! (for Monthly It would be months i.e, 2022-09 and for yearly It would be 2022)
![image](https://user-images.githubusercontent.com/72795959/188397321-16d96c99-8761-453e-8b45-b2f0e476b231.png)


### Backend

#### REST API  /repos

Getting Organization name and Number of Top Repositories to Display
![image](https://user-images.githubusercontent.com/72795959/188386609-752249e1-3311-4b9f-a8b3-d2842dca6ab1.png)

Getting Time Takken by One Request (ttbor), Calculating Number of pages (n) (due to pagination) to reach & Looping over pages to store values in result.
![image](https://user-images.githubusercontent.com/72795959/188386960-966dddad-589e-45ec-b31f-6cda76884968.png)

Sorting Result according to number of Starts & Adding a Final list to send a response
![image](https://user-images.githubusercontent.com/72795959/188387498-7f389199-aea5-4cbd-951e-e7235387c931.png)

Adding result, time takken by 1 request by github, Time takken by all requests Github, Time takken to send my response (after sorting etc)
![image](https://user-images.githubusercontent.com/72795959/188387917-7361244b-1469-4d18-842b-2f2fb4e1d9ca.png)

#### REST API /<<_org_>>/<<_repo_>>/commits

Getting Values of since, until & view from payload, Where Getting value of org & repo from path parameter itself.
![image](https://user-images.githubusercontent.com/72795959/188392953-72f59d64-7e49-4bfe-a432-b96bbc656ad2.png)

Adding Header, Constructing url, Getting Time takken by one & all responses respectively(ttbor, ttbar) & Calculating Number of pages (n) (due to pagination) to reach & Looping over pages to store values in result.
![image](https://user-images.githubusercontent.com/72795959/188393251-9346d52b-a905-4223-b118-f41dd2a4e31d.png)

Looping over pages by creating new request until last page is reached & storing data of every request to result
![image](https://user-images.githubusercontent.com/72795959/188393597-507a9faf-ef68-42d0-8115-2ff4cee7ca12.png)

Adding Result to final (response to be send) with response times.
![image](https://user-images.githubusercontent.com/72795959/188393692-084ab3f3-99c5-40c9-a50b-9581475136f3.png)


### Findings 

API's **/repos**: Response time Inscreases Exponentially according to the Organization (If organization have alot of repositories). Due to pagination complexity goes to O(n), Whereas it does not Depends on How many Top repositories you need, Because, It will still need to go through all the repositories.

