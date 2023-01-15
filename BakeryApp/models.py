from django.db import models
from django.contrib.auth.models import User
# Create your models here

class CategoryModel(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Products(models.Model):
    img_title = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    image = models.ImageField(upload_to='Images/')
    price = models.IntegerField()
    cat = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    Qua = models.IntegerField()

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=12)
    help = models.TextField(max_length=300)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product = models.TextField(default={'objects': []},null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    address = models.TextField(max_length=300,null=True,blank=True)
    contact = models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.user.username