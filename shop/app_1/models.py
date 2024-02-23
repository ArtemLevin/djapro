from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'Name:{self.name}, email:{self.email}, phone_number:{self.phone_number}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    add_date = models.DateTimeField(default=None)
    image = models.ImageField(null=True, default=None, blank=True, upload_to='media/')



class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(default=None)

    def show_all_products(self):
        return ', '.join([product.name for product in self.products.all()])


