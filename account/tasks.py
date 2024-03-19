from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from account.tokens import account_activation_token
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from core.models import *
from product.models import Image

def send_confirmation_mail(user, current_site):
    message = render_to_string('activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
    subject = 'Please confirm your account'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=[user.email,])
    mail.content_subtype = 'html'
    mail.send()


@shared_task
def send_subscirbers_mail():
    items = Image.objects.filter(variant__new_status=True).filter(is_main=True)
    email_list=Subscriber.objects.values_list("email",flat=True)
    message=render_to_string('email-subscribers.html', {
                "items": items
            })
    
    subject="Our new Products"
    mail= EmailMultiAlternatives(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER,to=email_list)
    mail.content_subtype='html'
    settings.EMAIL_HOST_USER
    
    mail.send()