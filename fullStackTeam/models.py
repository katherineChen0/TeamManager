from django.db import models

class Member(models.Model):
    ROLE_CHOICES = [
        ('Regular', 'Regular'),
        ('Admin', 'Admin'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Regular')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
