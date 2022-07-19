from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from helpers.models import BaseModel



class Category(BaseModel):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="category/", null=True)

    def __str__(self):
        return self.name


class Company(BaseModel):
    name = models.CharField(max_length=70)
    logo = models.ImageField(upload_to="company/")
    desription = models.TextField()
    view_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=800)
    # description = RichTextField()
    description = models.TextField()
    image = models.ImageField(upload_to="post/", null=True)
    view_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    



class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment

class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_liked = models.BooleanField()
