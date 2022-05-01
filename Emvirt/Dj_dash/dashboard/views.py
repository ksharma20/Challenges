from django.http import HttpResponse
from django.shortcuts import render
from .models import machine

# Create your views here.
def home(request):
    obj = None
    if request.method == "POST":
        name = request.POST.get('name')
        dtype = request.POST.get('type')
        print("Name = ",name, "\nDtype = ", dtype)
        obj = machine.objects.create(name=name, dtype=dtype)


    machines = machine.objects.all()
    if obj:
        context = {
            "machines" : machines,
            "message" : {
                "name" : obj.name, 
                "dtype" : obj.dtype
                }
        }
        obj.save()
    else:
        context = {
            "machines" : machines
        }

    return render(request, 'home.html', context)

def detail(request, pk):
    try:
        machinedt = machine.objects.get(pk=pk)
        context = {
            "machine" : machinedt
        }
        return render(request, 'detail.html', context)
    except:
        return HttpResponse("This is not a valid machine ID")