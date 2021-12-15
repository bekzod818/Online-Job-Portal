from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    salary = models.PositiveIntegerField(null=True)
    experience = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name


class Candidates(models.Model):
    category = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
    )
    name = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=200, null=True, choices=category)
    mobile = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    resume = models.FileField(null=True)
    company = models.ManyToManyField(Company, blank=True)

    def __str__(self):
        return self.name


