import secrets
from django.core.mail import send_mail
from django.conf import settings

def send_secret_code_email(email, code):
    """Send a secret code to the user's email."""
    subject = 'Your Secret Code'
    message = f'Your secret code is: {code}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)




def generate_secret_code(length=6):
    """Generate a random numeric secret code."""
    return ''.join(secrets.choice('0123456789') for _ in range(length))

