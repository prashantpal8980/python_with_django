from django.db import models
from django.utils import timezone

# Create your models here.
class TellTheStroy(models.Model):
    # GROUP_MEMBERS=[
    #     ('PP', 'Prashant Pal'),
    #     ('AP', 'Aashsih Patel'),
    #     ('BP', 'Bittu Kumar'),
    #     ('DJ', 'Deepak Jha'),
    # ]
    GROUP_MEMBERS=[
        ('Prashant Pal', 'Prashant Pal'),
        ('Ashish Patel', 'Ashsih Patel'),
        ('Bittu Kumar', 'Bittu Kumar'),
        ('Deepak Jha', 'Deepak Jha'),
    ]
    name = models.CharField(max_length=20, choices=GROUP_MEMBERS)
    story= models.TextField(max_length=1000,default='Once upon a time...')
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
