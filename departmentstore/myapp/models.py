from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.
CATEGORY=(
    ('Food','Food'),
    ('Drink','Drink'),
    ('Stationary','Stationary'),
    ('Cosmetic','Cosmetic'),

)

class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30,choices=CATEGORY,null=True)
    quantity = models.PositiveBigIntegerField()
    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}--{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'


    def __str__(self):
        return f'{self.product } Ordered by { self.staff.username}'

