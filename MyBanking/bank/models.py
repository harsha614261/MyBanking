from django.db import models

# Create your models here.
class Query(models.Model):
    objects=models.Manager()
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Contact=models.CharField(max_length=100)
    Querymes=models.TextField(max_length=100)
class transaction(models.Model):
    objects=models.Manager()
    Name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    account=models.TextField()
    amount = models.IntegerField()
    message=models.TextField(max_length=1000000)


