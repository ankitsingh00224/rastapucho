from django.db import models
from datetime import datetime

# Create your models here.

class Card(models.Model):
    tannu = models.CharField(max_length=100)
    mannu = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='images')
    creation_date = models.DateTimeField("date published",default=datetime.now())
    urls1 = models.CharField(max_length=250)

class TopCard(models.Model):
    title2 = models.CharField(max_length=100)
    image2 = models.ImageField(upload_to='images')
    description2 = models.TextField()
    urls2 = models.CharField(max_length=250)

class RecentCard(models.Model):
    title3 = models.CharField(max_length=100)
    image3 = models.ImageField(upload_to='images')
    address = models.CharField(max_length=200)
    urls3 = models.CharField(max_length=250)
    price = models.IntegerField(blank=True, null=True)


class BlogSlug(models.Model):
    slug_title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=1000)
    slug_content = models.CharField(max_length=250)
    published_date = models.DateTimeField("date published",default=datetime.now())

    class Meta:
        verbose_name_plural = "slugs"

    def __str__(self):
        return self.slug_title


class Blog(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()

    slug_title = models.ForeignKey(
        BlogSlug, default=1, on_delete=models.SET_DEFAULT)

    slug = models.CharField(max_length=500, default=1)

    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(default=datetime.now())
    your_image =  models.ImageField(upload_to='review',blank=True,null=True)

    def __str__(self):
        return str(self.name)
