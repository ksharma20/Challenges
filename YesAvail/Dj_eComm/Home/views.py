from django.contrib.auth.models import User
from Home.serializers import UserSerializer, CartSerializer, OrdersSerializer
from Home.models import Cart, Orders
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
def home(request):
    doc = '''
    <center><h1>Follow the Links to check APIs</h1><center>
    <p><a href='/login/'> Login - /login/ </a> </p>
    <p><a href='/signup/'> signup - /signup/ </a> </p>
    <p><a href='/cart/'> Cart - /cart/ </a> </p>
    <p><a href='/orders/'> Orders - /orders/ </a> </p>
    <p><a href='/product/list/'> Product List - /product/list/ </a> </p>
    <p><a href='/product/1/'> Product Details - /product/{product_id}/ </a> </p>
    '''
    return HttpResponse(doc)

@api_view(['POST','GET'])
def ulogin(request):
    users = User.objects.all()
    if request.method == 'GET':
        userSerializer = UserSerializer(users, many=True)
        return Response(userSerializer.data)
    
    if request.method == 'POST':

        if request.user.is_authenticated:
            logout(request)

        data = request.data
        user = authenticate(request,username=data['username'], password=data['password'])
        if user:
            login(request,user)
            return HttpResponse("Loged In",status=200)
        else:
            return HttpResponse("User Not Found", status=400)
    

@api_view(['POST','GET'])
def uregister(request):
    if request.method == 'GET':
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)
        return Response(userSerializer.data)
    
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        print(username)
        user,created = User.objects.get_or_create(username=username)
        if created:
            passwd = data.get('password')
            user.set_password(passwd)
            user.email = data.get('email')
            user.save()
            return HttpResponse('User Created', status=201)
        else:
            return HttpResponse("Username already Exists", status=402)


@api_view(['GET','POST'])
def cart(request):
    if request.user.is_authenticated:
        uCart, created = Cart.objects.get_or_create(user = request.user)
        if created:
            return HttpResponse("Cart Is Empty <br><br> <a href='/'>Goto Home</a>")

        if request.method == 'POST':
            data = request.data
            address = data['address']
            order = Orders.objects.create(user=request.user, address=address)
            for product in uCart.products.all():
                order.products.add(product)
            order.save()
            uCart.delete()
            return HttpResponse(f"Checkout Done for {order}", status=200)
        
        uCartSerializer = CartSerializer(uCart)
        return Response(uCartSerializer.data)
    else:
        return HttpResponse("User Not logged in", status=401)

@api_view(['GET'])
def orders(request):
    if request.user.is_authenticated:
        try:
            order = Orders.objects.filter(user = request.user)
        except:
            return HttpResponse("No order list available")

        orderSerializer = OrdersSerializer(order, many=True)
        return Response(orderSerializer.data)
    else:
        return HttpResponse("User Not logged in", status=401)

