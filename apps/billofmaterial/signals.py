from django.core.mail import send_mail
from django.urls import reverse
from django.utils.html import format_html
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BillOfMaterial

from django.template.loader import render_to_string


# @receiver(post_save, sender=BillOfMaterial)
# def send_bom_email(sender, instance, created, **kwargs):
#     if created:
#         subject = f"BOM {instance.id} submitted for review"
#         message = f"Please review BOM {instance.id} that has been submitted for review."
#         from_email = 'ingale.mandar@outlook.com'
#         recipient_list = ['ingale.mandar@outlook.com']
#         send_mail(subject, message, from_email, recipient_list, fail_silently=False)


@receiver(post_save, sender=BillOfMaterial)
def send_bom_email(sender, instance, created, **kwargs):
    if created:
        subject = f"BOM {instance.id} submitted for review"
        template = 'bom_submission.html'
        context = {
            'approver_name': 'John Doe',
            'bom_name': instance.name,
        }
        html_message = render_to_string(template, context)
        from_email = 'ingale.mandar@outlook.com'
        recipient_list = ['ingale.mandar@outlook.com']
        send_mail(subject, message='', from_email=from_email, recipient_list=recipient_list, html_message=html_message, fail_silently=False)
