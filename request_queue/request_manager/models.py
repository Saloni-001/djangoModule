# request_manager/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .management.commands.process_requests import Command

class Request(models.Model):
    request_data = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request_data

@receiver(post_save, sender=Request)
def start_processing(sender, instance, created, **kwargs):
    if created:
        Command().handle()
