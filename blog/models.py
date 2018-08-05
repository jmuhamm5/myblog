from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField('blog.Category', blank=False)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    parent = models.ForeignKey('blog.Category', on_delete=models.CASCADE, blank=True, null=True)

    @staticmethod
    def list_categories():
        return Category.objects.all()

    def __str__(self):
        return self.title