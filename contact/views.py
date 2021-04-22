from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def contact(request):
    """A view that allows potential customers to send an
    email message and then redirect to the contact page"""

    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            email_address = contact_form.cleaned_data['email_address']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, email_address,
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('email_success')
    return render(request, "contact/contact.html",
                  {'contact_form': contact_form})


def email_success(request):

    template = 'contact/email_success.html'

    return render(request, template)
