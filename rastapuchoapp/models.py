from django.db import models

# Create your models here.

class Card(models.Model):
    tannu = models.CharField(max_length=100)
    mannu = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='images')
    urls1 = models.CharField(max_length=250)

class TopCard(models.Model):
    title2 = models.CharField(max_length=100)
    image2 = models.ImageField(upload_to='images')
    description2 = models.TextField()
    urls2 = models.CharField(max_length=250)
