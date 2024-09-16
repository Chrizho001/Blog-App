# views.py (in the admin or a separate view for sending the newsletter)
from django.core.mail import send_mail
from .models import Subscriber

def send_newsletter():
    subscribers = Subscriber.objects.all()
    emails = [subscriber.email for subscriber in subscribers]
    subject = 'this is a test'
    message = 'Hi i sent this from django'
    send_mail(
        subject,  # Subject of the email
        message,  # Body of the email
        'fridaychristopher.jr@gmail.com',  # From email
        emails,  # List of recipient emails
        fail_silently= False
    )
