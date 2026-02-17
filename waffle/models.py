from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class WaffleVariety(models.Model):
    WAFFLE_TYPE_CHOICE =  [
        ('CL', 'CHOCOLATE'),
        ('VL', 'VANILLA'),
        ('TC', 'TRIPLE CHOCOLATE'),
        ('MC', 'MILK CHOCOLATE'),
        ('DC', 'DARK CHOCOLATE')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'waffleis/')
    date_added = models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length=2, choices = WAFFLE_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name



#one to many 

class WaffleReviews(models.Model):
    waffle = models.ForeignKey(WaffleVariety , on_delete=models.CASCADE, related_name = 'reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.waffle.name}'
    


# many to many

class Store (models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField( max_length=70)
    waffle_varieties = models.ManyToManyField(WaffleVariety, related_name ='stores')

    def __str__(self):
        return self.name
    

# one to one 

class WaffleCertificate (models.Model):
    waffle = models.OneToOneField(WaffleVariety, on_delete=models.CASCADE, related_name = 'certificate')
    certificate_number = models.CharField(max_length=50)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.waffle}'
    

    
