from django.db import models
from django.utils import timezone

class Contact(models.Model):
    contact_name = models.CharField(max_length=255)
    email = models.EmailField()
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.contact_name

