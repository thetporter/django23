from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
       
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='main/images')
    url = models.URLField(blank=True)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    categories = models.ManyToManyField(Category, related_name='blogs', blank=True)

    

