from django.db import models

# Create your models here.

#Django creates a unique value automatically for each row, whenever it is entered
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    #this returns username whenever "User.objects.all()" is run
    def __str__(self): #
        return  self.username

class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField
    imageurl = models.CharField(max_length=1000)
