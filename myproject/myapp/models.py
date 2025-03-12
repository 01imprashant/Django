from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class myapp_variety(models.Model):
    APP_TYPE_CHOICE=[
        ('W','WHATSAPP'),
        ('I','INSTAGRAM'),
        ('F','FACEBOOK'),
        ('A','AMAZON'),
        ('Z','ZEPTO'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='myapp/')
    date=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=APP_TYPE_CHOICE)
    description=models.TextField(default='')

    def __str__(self):
        return self.name


# One-to-many

class app_review(models.Model):
    ALL_RATING_TYPE=[
        ('1','*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'),
    ]
    app = models.ForeignKey(myapp_variety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=2,choices= ALL_RATING_TYPE)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.app.name}'
    

# Many-to-many

class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    app_varieties = models.ManyToManyField(myapp_variety, related_name='stores')

    def __str__(self):
        return self.name


# One-to-one

class app_certificate(models.Model):
    app = models.OneToOneField(myapp_variety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.app}'
