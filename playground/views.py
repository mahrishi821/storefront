# views are more like request handler in django
from django.shortcuts import render
from store . models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from . import templates

# Create your views here.

def say_hello(request):

    # query_set=Product.objects.all() # hjere django will not run the query set , it will run when it's used
    #example
    # here objects is the manager of the database
    #in the query set we can apply filter and order by
    #if we have used q=product.objects.count() it will return a integer

    # for product in query_set:
    #     print(product)
    # The query set will be evaluated at the
    # list(query_set)
    # or when we try get some particular element from the query set
    # try:
    #     product = Product.objects.get(pk=-0)
    # except ObjectDoesNotExist:
    #     pass
    product=Product.objects.filter(pk=0).first() # here it will not throw any exception it will give None value



    return render(request,'hello.html',{'name':'rishi'})

