from django.db import models
from  django.contrib.auth.models import User
from  django.urls  import  reverse
from  django.utils.six import python_2_unicode_compatible
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=70)
class  Tag(models.Model):
    name=models.CharField(max_length=70)
@python_2_unicode_compatible
class  Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt=models.CharField(max_length=70,blank=True)
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag)
    author=models.ForeignKey(User)
    def  __str__(self):
        return self.title
    def  get_absolute_url(self):
        return   reverse("blog:detail",kwargs={'pk':self.pk})
