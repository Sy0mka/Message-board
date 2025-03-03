from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Response
from django.core.mail import send_mail

@receiver(post_save, sender=Response)
def notify_on_response(sender, instance, created, **kwargs):
    if created:
        subject = 'Новый отклик на ваше объявление'
        message = f'Пользователь {instance.author.email} оставил отклик: {instance.text}'
        send_mail(
            subject,
            message,
            'noreply@mmorpg-board.com',
            [instance.ad.author.email],
            fail_silently=False,
        )