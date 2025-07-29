from django.db import models
from users.models import Student
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ShopHistory(models.Model):
    STATUSES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Cancelled', 'Cancelled'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUSES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name