from django.db import models
from Authentication.models import User

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(null=True, max_length=20)
    profile_picture = models.ImageField(upload_to='admin_profile/', blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    post = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255,  null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100,  null=True)
    department = models.CharField(max_length=100, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post}'
