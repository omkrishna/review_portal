from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils import timezone

class Course(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    branch = (
        ('AM', 'Applied Mechanics'),
        ('BB', 'Biochemical Engineering and Biotechnology'),
        ('CH', 'Chemical Engineering'),
        ('CE', 'Civil Engineering'),
        ('CS', 'Computer Science and Engineering'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
    )
    title = models.CharField(max_length = 6)
    department = models.CharField(max_length=2, choices=branch)
    def __str__(self):
        return self.title

class Professor(models.Model):
    branch = (
        ('AM', 'Applied Mechanics'),
        ('BB', 'Biochemical Engineering and Biotechnology'),
        ('CH', 'Chemical Engineering'),
        ('CE', 'Civil Engineering'),
        ('CS', 'Computer Science and Engineering'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
    )

    title = models.CharField(max_length = 40 )
    department = models.CharField(max_length=2, choices=branch)
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title



class Review(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    P_name = models.ForeignKey(Professor, on_delete=models.CASCADE)
    quality = models.IntegerField(default=0, 
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    difficulty = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    would_take_again = models.BooleanField(default=False)
    comments = models.TextField()
    overall = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])



	
 
 