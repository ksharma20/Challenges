from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Home.models import Cart
from Product.models import Product
from Product.serializers import ProductSerializer

# Create your views here.
def index(request):
    doc = '''
    <center><h1>Follow The Links to check APIs</h1><center>
    <p><a href='/login/'> Login - /login/ </a> </p>
    <p><a href='/signup/'> signup - /signup/ </a> </p>
    <p><a href='/cart/'> Cart - /cart/ </a> </p>
    <p><a href='/orders/'> Orders - /orders/ </a> </p>
    <p><a href='/product/list/'> Product List - /product/list/ </a> </p>
    <p><a href='/product/2/'> Product Details - /product/{product_id}/ </a> </p>
    '''
    return HttpResponse(doc)

@api_view(['GET'])
def list(request):
    products = Product.objects.all()
    pSerializer = ProductSerializer(products, many=True)
    return Response(pSerializer.data)

@api_view(['POST', 'GET'])
def detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return HttpResponse("Product ID Does not Exist")
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user = request.user)
            cart.products.add(product)
            cart.save()
            return HttpResponse("Product Added to Cart")
        else:
            return HttpResponse("User Not logged In")
    
    pSerial = ProductSerializer(product)
    return Response(pSerial.data)