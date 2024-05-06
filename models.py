from django.db import models

# Create your models he
class op(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class teacher(models.Model):
  name = models.CharField(max_length=255)
  mobile=models.IntegerField()
  email=models.EmailField( max_length=254)