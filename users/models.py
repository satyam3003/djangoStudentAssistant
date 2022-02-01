from django.db import models
from django.contrib.auth.models import User
from course.models import *


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prn = models.CharField(max_length=120)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.prn} - {self.user}"

# class RegisterCourse(models.Model):
#     userprof = models.ManyToManyField(Profile)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.userprof} - {self.course}"
