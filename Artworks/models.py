from django.db import models
from Authentication.models import User
from django.core.exceptions import ValidationError
# Create your models here.

    
class Artwork(models.Model):
    MEDIUM_CHOICES = [
        ('painting', 'Painting'),
        ('sculpture', 'Sculpture'),
        ('photography_digital', 'Digital Photography'),
        ('photography_film', 'Film Photography'),
        ('digital_painting', 'Digital Painting'),
        ('3d_modeling', '3D Modeling'),
        ('vr_art', 'Virtual Reality Art'),
        ('ar_art', 'Augmented Reality Art'),
        ('digital_collage', 'Digital Collage'),
        ('generative_art', 'Generative Art'),
    ]
    STYLE_CHOICES = [
        ('modern', 'Modern'),
        ('expressionism', 'Expressionism'),
        ('realism', 'Realism'),
        ('abstract', 'Abstract'),

    ]
    GENRE_CHOICES = [
        ('landscape', 'Landscape'),
        ('portrait', 'Portrait'),
        ('conceptual', 'Conceptual'),
        ('figurative', 'Figurative'),
        ('street', 'Street'),
        ('documentary', 'Documentary'),
    ]
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='arts', null=True, blank=True, limit_choices_to={'is_artist': True})
    medium = models.CharField(max_length=100, choices=MEDIUM_CHOICES, null=True, blank=True)
    year_created = models.DateField()
    image = models.ImageField(upload_to='image/', null=True)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, null=True, blank=True)
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, null=True, blank=True)
    price_range_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_range_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    artworks = models.ManyToManyField('Artwork', related_name='wishlisted_by')

    def __str__(self):
        return f'{self.user.username} Wishlist'
