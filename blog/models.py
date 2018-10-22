from django.db import models
from datetime import datetime
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name_plural = 'tableA'

#class Login(models.Model):
#    username = models.CharField(max_length = 50)
#    password = models.CharField(max_length = 50)

# class SignUp(models.Model):
#     name = models.CharField(max_length = 50)
#     email = models.CharField(max_length = 50)
#     username = models.CharField(max_length = 50)
#     password = models.CharField(max_length = 50)
