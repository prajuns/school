from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=200)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female')
    )
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    address=models.TextField()
    department=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    purpose=models.CharField(max_length=20)
    material=models.CharField(max_length=20)
