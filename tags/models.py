from django.db import models
from django.contrib.contenttypes.models import  ContentType
from django.contrib.contenttypes.fields import  GenericForeignKey
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    label=models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    #Type of the object(product,Video,article)
    #Id of the object
    # here we are not specing the particular model of the store app but here we are using
    # the ContentType of the generic model provided by the django
    #CotentType use to create Generic relationships
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey() #it will the actual data for which the tagged is applied to





