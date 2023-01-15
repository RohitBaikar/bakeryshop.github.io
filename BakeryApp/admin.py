from django.contrib import admin
from . models import *

# Register your models here.


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']

@admin.register(Products)
class ImageAdmin(admin.ModelAdmin):
    list_display=['img_title','details', 'image','price', 'cat','Qua']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['name','email','contact','help']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['user','product','created','updated']

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['user','address','contact']


