from django.db import models

    

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'IN_PROGRESS'),
        ('COMPLETED', 'Completed'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    annotations = models.JSONField(null=True, blank=True)  # New field for annotations
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
