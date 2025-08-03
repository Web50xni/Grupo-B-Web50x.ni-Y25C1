from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Studyspaces(models.Model):
    title = models.CharField(blank=False, max_length=25)
    description = models.TextField(blank=True)
    goal = models.CharField(blank=True, max_length=75)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    
class Notes(models.Model):
    title = models.CharField(blank=False, max_length=25)
    content = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    studyspace = models.ForeignKey(Studyspaces, related_name='notes', on_delete=models.CASCADE)
