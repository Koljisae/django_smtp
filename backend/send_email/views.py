from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Contact
from .tasks import (
    send_newsletter_email_task,
)


@login_required
def send_subscription_email(request):
    try:
        if Contact.objects.filter(user=request.user, subscribed_mail=False).exists():
            contact_user = Contact.objects.filter(user=request.user, subscribed_mail=False).get()
            subject = 'You are subscribed to the newsletter!'
            message = 'You have subscribed to the newsletter!'
            send_newsletter_email_task.delay(request.user.email, subject, message)
            contact_user.subscribed_mail = True
            contact_user.save()
            response = 'You have subscribed to the newsletter!'
            return render(request, 'user/response.html', {'response': response})
        elif Contact.objects.filter(user=request.user, subscribed_mail=True).exists():
            response = 'You already subscribed to the newsletter!'
            return render(request, 'user/response.html', {'response': response})
        else:
            response = 'Error! Re-log in.'
            template = render(request, 'user/response.html', {'response': response})
            template.status_code = 404
            return template
    except Exception:
        response = 'Error!'
        template = render(request, 'user/response.html', {'response': response})
        template.status_code = 404
        return template


@login_required
def send_unsubscribe_email(request):
    try:
        if Contact.objects.filter(user=request.user, subscribed_mail=True).exists():
            contact_user = Contact.objects.filter(user=request.user, subscribed_mail=True).get()
            subject = 'You have unsubscribed from the newsletter!'
            message = 'You have unsubscribed from the newsletter!'
            send_newsletter_email_task.delay(request.user.email, subject, message)
            contact_user.subscribed_mail = False
            contact_user.save()
            response = 'You have unsubscribed from the newsletter!'
            return render(request, 'user/response.html', {'response': response})
        elif Contact.objects.filter(user=request.user, subscribed_mail=False).exists():
            response = 'You are not subscribed to the newsletter!'
            return render(request, 'user/response.html', {'response': response})
        else:
            response = 'Error! Re-log in.'
            template = render(request, 'user/response.html', {'response': response})
            template.status_code = 404
            return template
    except Exception:
        response = 'Error!'
        template = render(request, 'user/response.html', {'response': response})
        template.status_code = 404
        return template

