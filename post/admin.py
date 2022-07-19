from django.contrib import admin

from post.models import Category, Post, Company, Review

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Review)