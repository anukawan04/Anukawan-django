from django.db import models

# Create your models here.

class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    order_name = models.CharField(max_length=100)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')


    p = models.CharField(max_length=50, blank=True, null=True)
    c = models.CharField(max_length=50, blank=True, null=True)
    f = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.order_name} (User: {self.user.full_name})"
