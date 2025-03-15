from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class project_variety(models.Model):
    PROJECT_TYPE=[
        ('1','General Project'),
        ('2','Social Project'),
        ('3','Welfare Project'),
        ('4','Schlores Project'),
        ('5','Consumer Project'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='app/')
    date=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=PROJECT_TYPE)
    
    def __str__(self):
        return self.name


# One-to-Many Relation
class project_review(models.Model):
    project = models.ForeignKey(project_variety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=5)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.project.name}'
    

# Many-to-Many Relation
class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    project_varieties = models.ManyToManyField(project_variety, related_name='stores')

    def __str__(self):
        return self.name


# One-to-One Relation
class project_certificate(models.Model):
    project = models.OneToOneField(project_variety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.project}'
