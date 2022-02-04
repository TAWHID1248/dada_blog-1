from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name




class Post(models.Model):
    title = models.CharField(max_length=250) 
    featured = models.BooleanField(default=False)
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)



    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

        
    def yearpublished(self):
        return self.post_date.strftime('%Y')

    

