from django.db import models

# Create your models here.

# Class to SQL --> Database a hit korbe
class Blog(models.Model): #Database a Blog name a ekta Table create korbe
    name = models.TextField() # name field create hobe
    image = models.ImageField(upload_to='media', blank=True,null = True)
# Command
# Class --> SQL a convert korbe
# python manage.py makemigrations 

# Command
# SQL ke Database a kaj korano
# python manage.py migrate
 
    def __str__(self):
        return f"Blog No {self.id}. {self.name}"
    
#Template ->Ui/Ux part handle kore
# dui vhabe kora jai
# 1.globally  
# 2.Inner app folder  -->settings.py a jobabdihi kora lagbe na
#static file ->future a change hobe na
#media files -> dynamically change hobe