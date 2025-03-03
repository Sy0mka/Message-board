from celery import shared_task
from django.core.mail import send_mass_mail
from users.models import CustomUser

@shared_task
def send_newsletter_task(subject, message):
    users = CustomUser.objects.filter(is_verified=True)
    messages = [(subject, message, 'noreply@example.com', [user.email])
                for user in users]
    return send_mass_mail(messages, fail_silently=False)