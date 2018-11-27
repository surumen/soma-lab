from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)

def ants_and_bees(request):
    context={}
    return render(request,'ants_and_bees.html',context)