from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout, authenticate
from .serializers import User, Task, TaskSerializer

# Create your views here.


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
            return Response('loged-out')
        uname = request.data.get('email')
        passwd = request.data.get('password')
        print("Login --> ", uname, passwd)
        if uname and passwd:
            user = authenticate(request, username=uname, password=passwd)
            if user:
                login(request, user)
                return Response('Loged-in')
        else:
            return Response('Invalid email or password')
    return Response('log-in Or log-out')


@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
            return Response('loged-out')
        uname = request.data.get('email')
        passwd = request.data.get('password')
        print("Register --> ", uname, passwd)
        if uname and passwd:
            user, created = User.objects.get_or_create(username=uname)
            if created:
                user.set_password(passwd)
                user.save()
                return Response('User Created')
        else:
            return Response('Email already Exist')
    return Response('Sign Up')


@api_view(['POST'])
def create_task(request):
    if request.user.is_authenticated:
        name = request.data.get('task')
        desc = request.data.get('description')
        print("Create task --> ", name, desc)
        if desc:
            task = Task.objects.create(
                user=request.user, name=name, description=desc)
        else:
            task = Task.objects.create(user=request.user, name=name)
        return Response(f'Task -->{task.name}<-- Created at -->{task.created_at}<-- ')
    return Response('Please login Before Creating a task')


@api_view(['GET'])
def view_tasks(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        print("View Tasks --> ", tasks)
        taskSerialize = TaskSerializer(tasks, many=True)
        return Response(taskSerialize.data)
    return Response('Please login Before Viewing a task')


@api_view(['GET', 'POST'])
def view_task(request, pk):
    if request.user.is_authenticated:
        task = Task.objects.get(pk=pk)
        print("View Task --> ", task)
        if request.method == 'POST':
            rdata = request.data.get('option').lower()
            print("rdata-> ", rdata)
            if 'del' in rdata:
                task.delete()
                return Response('Task Deleted')
            elif 'mark' in rdata or 'com' in rdata:
                task.completed = True
                task.save()
                return Response('Task Marked as Completed')
        taskSerialize = TaskSerializer(task)
        return Response(taskSerialize.data)
    return Response('Please login Before Viewing a task')
