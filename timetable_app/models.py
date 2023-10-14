# timetable_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional user-related fields

class Course(models.Model):
    name = models.CharField(max_length=255)
    # Add other course-related fields as needed

class Timetable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=50)

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
