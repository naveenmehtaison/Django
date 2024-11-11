from django.db import models
from django.utils import timezone

class ChaiVarity(models.Model):
    CHAI_TYPE_VOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN')
    ]
    name_nam = models.CharField( max_length=100)
    # image = models.ImageField( default= 'naveen' , upload_to='chais/')
    # date_added =models.DateTimeField(default=timezone.now)
    # Name = models.CharField(max_length=1000)
    
    type=models.CharField(max_length=2, choices=CHAI_TYPE_VOICE)
    
def __str__(self):
    return self.name





# Create your models here.
