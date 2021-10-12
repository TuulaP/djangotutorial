from django.db import models
from relativefilepathfield.fields import RelativeFilePathField
import os
from decouple import config

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)

    absflagpath = os.path.join(config("BASE_DIR"),'static/img/')
    
    image = models.FilePathField(path=absflagpath)
    

