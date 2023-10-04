from django.db import models

# Create your models here.


class UserData(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100)
    EmailId = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Confirm_Password=models.CharField(max_length=100)
    

class PostData(models.Model):
    Post=models.CharField(max_length=500)
    UserName=models.CharField(max_length=100)