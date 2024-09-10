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
    title = models.CharField(max_length=100, null=True)
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='arts', null=True, blank=True, limit_choices_to={'is_artist': True})
    medium = models.CharField(max_length=100, choices=MEDIUM_CHOICES, null=True, blank=True)
    year_created = models.DateField(null=True)
    image = models.ImageField(upload_to='image/', null=True)
    description = models.TextField(max_length=2000, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, null=True, blank=True)
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        
        
        super().save(*args,**kwargs)

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    artworks = models.ManyToManyField('Artwork', related_name='wishlisted_by')

    def __str__(self):
        return f'{self.user.username} Wishlist'


from django.db import models
from django.utils import timezone
import datetime

    
class Exhibition(models.Model):
    title = models.CharField(max_length=200, null=True)
    start_date = models.DateField( null=True)
    end_date = models.DateField(null=True)
    curator = models.CharField(max_length=100, null=True)
    description = models.TextField( null=True)
    artworks = models.ManyToManyField('Artwork', related_name='exhibitions', blank=True, null=True)  # Many-to-Many relation with Artwork
    brief_description = models.CharField(max_length=300, null=True)
    thumbnail = models.ImageField(upload_to='exhibitions/thumbnails/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    @property
    def is_current(self):
        today = datetime.date.today()
        return self.start_date <= today <= self.end_date
    @property
    def is_upcoming(self):
        today = datetime.date.today()
        return today < self.start_date
