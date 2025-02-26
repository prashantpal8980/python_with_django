from django.db import models
from django.utils import timezone

# Create your models here.
class TellTheStroy(models.Model):
    GROUP_MEMBERS=[
        ('PP', 'Prashant Pal'),
        ('AP', 'Aashsih Patel'),
        ('BP', 'Bittu Kumar'),
        ('DJ', 'Deepak Jha'),
    ]
    name = models.CharField(max_length=2, choices=GROUP_MEMBERS)
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(default=timezone.now)

