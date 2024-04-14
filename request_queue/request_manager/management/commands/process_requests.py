# request_manager/management/commands/process_requests.py
import time
from django.core.management.base import BaseCommand
from request_queue.request_manager.models import Request

class Command(BaseCommand):
    help = 'Process the request queue'

    def handle(self, *args, **kwargs):
        while True:
            pending_requests = Request.objects.filter(status='Pending').order_by('timestamp')
            for req in pending_requests:
                # Simulate processing
                if req.id % 3 == 0:  # Introduce delay for every third request
                    time.sleep(2)  # Simulating processing time longer than 1 second
                else:
                    time.sleep(0.5)  # Simulating processing time less than 1 second
                req.status = 'Processed'
                req.save()
                print(f"Processed request: {req}")
            time.sleep(5)  # Check for pending requests every 5 seconds
