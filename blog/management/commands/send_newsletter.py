# send_newsletter.py

from django.core.management.base import BaseCommand
from send_mail import send_newsletter

class Command(BaseCommand):
    help = 'Send the newsletter to all subscribers'

    def handle(self, *args, **kwargs):
        subject = 'Our Latest Newsletter!'
        message = 'Hello! Here’s our latest content.'
        send_newsletter(subject, message)
        self.stdout.write(self.style.SUCCESS('Successfully sent the newsletter'))
