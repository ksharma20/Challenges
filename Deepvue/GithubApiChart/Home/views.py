from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html', {})

def dash(request):
    return render(request, 'dash.html', {})