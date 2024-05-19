from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    about = models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to='product_image', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return f"{self.name}"



class Gallary(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallary_image', null=True)

    def __str__(self):
        return f"{self.name}"