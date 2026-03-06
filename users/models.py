from django.db import models
from django.contrib.auth.models import AbstractUser

class Human(AbstractUser):
    fullname = models.CharField(max_length=50)
    picture = models.FileField(upload_to='media/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.username