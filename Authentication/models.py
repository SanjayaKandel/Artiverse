from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=False)
    is_artist = models.BooleanField('Is artist', default=False)


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist', null=True)
    name = models.CharField(max_length=255, null=True)
    profile_picture = models.ImageField(upload_to='artist_profiles/', null=True)
    biography = models.TextField(null=True)
    age=models.IntegerField(null=True)
    country=models.CharField(max_length=50, null=True)
    street=models.CharField(null=True, max_length=50)
    ward_no=models.IntegerField(null=True)
    category=models.CharField(max_length=100,  null=True)
    contact_phone = models.CharField(max_length=20, null=True)
    website = models.URLField(blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Artist"
