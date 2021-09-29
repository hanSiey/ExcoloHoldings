from django.db import models
from datetime import datetime
# Create your models here.

class GetQuote(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

class ContactMessage(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=1000)
    message_date = models.DateTimeField(default=datetime.now, blank=True)