import sys
sys.path.insert(1,"A://DJ//ecomm//ecomm//Util")
from utility_models import BaseModel

from django.db import models

# Create your models here.
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to="categories")
    slug = models.SlugField(unique=True, null=True, blank=True)

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()
    ription = models.TextField()
    slug = models.SlugField(unique=True,null=True,blank=True)
    
class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")
    image = models.ImageField(upload_to="product")    