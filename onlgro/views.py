from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    #print('hloooooooo')
    return HttpResponse('test data')

def TestFuncont(request):
    return render(request,'index.html')

