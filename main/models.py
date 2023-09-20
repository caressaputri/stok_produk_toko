from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()  # Add the description field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/')  # Tambahkan bidang gambar
