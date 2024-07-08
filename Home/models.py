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