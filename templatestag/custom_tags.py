
from django import template
from ..BakeryApp.models import Products
register = template.Library()

@register.filter()
def productimage(pid):
    data = Products.objects.get(id=pid)
    return data.image.url

@register.filter()
def productname(pid):
    data = Products.objects.get(id=pid)
    return data.name

@register.filter()
def productprice(pid):
    data = Products.objects.get(id=pid)
    return data.price

@register.simple_tag()
def producttotalprice(pid, qty):
    data = Products.objects.get(id=pid)
    return int(qty) * int(data.price)