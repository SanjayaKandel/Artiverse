from django.db import models
import datetime

class Exhibition(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    curator = models.CharField(max_length=100)
    description = models.TextField()
    brief_description = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to='exhibitions/thumbnails/')

    def __str__(self):
        return self.title

    def is_current(self):
        today = datetime.date.today()
        return self.start_date <= today <= self.end_date

    def is_upcoming(self):
        today = datetime.date.today()
        return today < self.start_date
