# views are more like request handler in django
from django.shortcuts import render
from . import templates

# Create your views here.

def say_hello(request):
    return render(request,'hello.html',{'name':'rishi'})
    # return HttpResponse('Hello World')
