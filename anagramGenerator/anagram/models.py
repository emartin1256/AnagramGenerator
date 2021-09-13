from django.db import models

# Create your models here.
class Anagram(models.Model):
    content = models.TextField()
