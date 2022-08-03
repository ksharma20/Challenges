from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, AuthUser
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@api_view(['POST'])
def ulogin(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
            return Response("Logged Out",200)

        data = request.data
        try:
            user = authenticate(request,username=data['username'], password=data['password'])
        except:
            return Response("Wrong combination of username & Password",400)
        if user:
            login(request,user)
            return Response("Logged In",200)

    return Response("User Not Found", status=400)
    

@api_view(['POST','GET'])
def uregister(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        print(username)
        user,created = User.objects.get_or_create(username=username)
        if created:
            passwd = data.get('password')
            user.set_password(passwd)
            user.first_name = data.get('first name')
            user.last_name = data.get('last name')
            user.save()
            print(type(request.FILES.get('profile pic')))
            print(int(data.get("phone number")))
            if request.FILES.get('profile pic'):
                try:
                    AuthUser.objects.create(user=user, pnum=int(data.get("phone number")), ppic=request.FILES['profile pic'])
                except:
                    return Response('Problem in Profile Pic', status=201)
            else:
                AuthUser.objects.create(user=user, pnum=int(data.get("phone number")))
            return Response('User Created Successfully', status=201)
        else:
            return Response("Username already Exists", status=402)
        
    users = User.objects.all()
    userSerializer = UserSerializer(users, many=True)
    return Response(userSerializer.data)

