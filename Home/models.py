from django.db import models
from Artworks . models import Artwork
from Authentication . models import User
# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.artwork.title} (x{self.quantity})"

    def get_total_price(self):
        return self.artwork.price * self.quantity
    
ORDER_STATUS = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled')
)
METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Esewa", "Esewa"),
)

class OrderedItem(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, verbose_name="artwork",null=True, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50,default="Pending", choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)
    transaction_uuid = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return "Order: " + str(self.id)
    
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name}'

