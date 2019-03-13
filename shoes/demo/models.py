from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=11)
    def __str__(self):
        return self.name


class Shoes(models.Model):
    color=models.CharField(max_length=20)
    size=models.CharField(max_length=11)
    u=models.ForeignKey(to=User,on_delete=models.CASCADE)
