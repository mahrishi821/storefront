from django.urls import path
from . import views

#url config each app have it's own url configrations
#urlpatterns is the variable for which the django look for
urlpatterns=[
    path('hello/',views.say_hello)
]