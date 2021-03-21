from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=50)

    YEAR_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    ]
    gender = models.CharField(choices=YEAR_CHOICES, default='male', max_length=10)
    dob = models.DateTimeField()
    blood_group = models.CharField(default="", max_length=6)
    age = models.IntegerField()
    contact_no = models.IntegerField()
    address = models.CharField(default="", max_length=80)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=30, default = "")
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=50)

    YEAR_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    ]
    gender = models.CharField(choices=YEAR_CHOICES, default='male', max_length=10)
    specialization = models.CharField(default="", max_length=30)
    age = models.IntegerField()
    contact_no = models.IntegerField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class History(models.Model) :
    date = models.DateTimeField()
    complication = models.CharField(max_length=50, default = "")
    doctor = models.CharField(max_length=30)
    patient = models.CharField(max_length=30)
    prescription = models.CharField(max_length=500)


    
