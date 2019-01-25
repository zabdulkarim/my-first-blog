# Create your models here. Define all objects - this is a place in which we will define our blog post.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #Here we are defining an Object named 'Post'. The content in the brackets is so that Django knows its a Django Model and to save in the DB.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #This section defines the properties.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null=True)

    def publish(self): #this is the publish method. Ruling is to use lowercase and underscores for methods.
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #Methods often return something, when we call __str__ we will get text(string) with a Post title.
        return self.title




