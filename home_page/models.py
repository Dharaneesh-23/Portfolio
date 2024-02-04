from django.db import models

# Create your models here.
class welcome(models.Model):
    link = models.TextField()
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=400)

class about(models.Model):
    abt = models.CharField(max_length=200)
    desc = models.TextField()
    ph = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

class links(models.Model):
    logo = models.CharField(max_length=50)
    link = models.CharField(max_length=200)

class education(models.Model):
    year = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    place = models.CharField(max_length=250)
    desc = models.CharField(max_length=400)

class projects(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='projectPics')
    p_link = models.CharField(max_length=300)

class experience(models.Model):
    duration = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    desc = models.TextField()

class skills(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=120)

class Contact_message(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    message = models.TextField()