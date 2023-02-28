from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    
    CHOICES_PRIORITY =(
        (LOW,'Low'),
        (MEDIUM,'Medium'),
        (HIGH,'High'),
    )
    NEW = 'new'
    CONTACTED = 'contacted'
    LOST = 'lost'
    WON = 'won'
    
    CHOICES_STATUS = (
        (NEW,'New'),
        (CONTACTED,'Contacted'),
        (LOST,'Lost'),
        (WON,'Won'),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=10,choices=CHOICES_STATUS,default=NEW)
    converted_to_client = models.BooleanField(default=False)
    priority = models.CharField(max_length=10,choices=CHOICES_PRIORITY,default=MEDIUM)
    created_by = models.ForeignKey(User,related_name='leads',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
