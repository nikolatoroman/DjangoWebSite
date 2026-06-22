from django.db import models

class Product(models.Model):
    PLATFORM_CHOICES = [
        ('PS4', 'PlayStation 4'),
        ('PS5', 'PlayStation 5'),
        ('XBOX', 'Xbox'),
    ]

    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title