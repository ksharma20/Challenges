from django.http.response import HttpResponse, JsonResponse
from task.models import UData
from task.serializers import UDataSerializer
# from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view 
# Create your views here.
def index(request):
    return HttpResponse("<center><h1>Follow your Defined Routes <br> Made By Keshav Sharma <br> For Backend Development (Django) internship at Impulse Edu Group")

@api_view(['GET'])
def tall(request):
    UDatas =UData.objects.all()
    serializer =UDataSerializer(UDatas, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def tnew(request):
    data = JSONParser().parse(request)
    serializer =UDataSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)