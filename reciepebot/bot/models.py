from django.db import models

class OrderArchive(models.Model):
    from_number = models.CharField(max_length=20)
    pdf_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    quantity = models.FloatField()
    description = models.CharField(max_length=255)
    price = models.FloatField()

class UserSession(models.Model):
    from_number = models.CharField(max_length=255, unique=True)
    order_items = models.ManyToManyField(OrderItem, blank=True)
    state = models.CharField(max_length=50, default='waiting_for_quantity')

    def __str__(self):
        return f"Session {self.from_number} - State: {self.state}"