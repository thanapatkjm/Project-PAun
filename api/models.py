from django.db import models
from datetime import datetime    
from django.utils import timezone

class refridgerator_display_system(models.Model):
    name = models.TextField()
    id = models.TextField(primary_key=True)
    status = models.TextField()
    datetime = models.DateTimeField(default=timezone.now())
