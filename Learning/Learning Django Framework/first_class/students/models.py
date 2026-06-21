from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(unique = True)
    grade = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to ='profile_pics/', blank=True,null=True)
    dob = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
    
class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(unique = True)
    grade = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to ='profile_pics/', blank=True,null=True)
    
    def __str__(self):
        return self.name     