from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail


def contact(request):
    """A view that allows potential customers to send an
    email message and then redirect to the contact page"""

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            messages.success(request, "Your message was sent successfully.\
                Please allow up to 1 working week for a response.")

            send_mail(
                request.POST['email_address'],
                request.POST['message'],
                "Robert Clark Design",
                ['robertclarkdesign@outlook.com'],
                fail_silently=False,
            )

            return HttpResponseRedirect('contact')

    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form
    }

    return render(request, template, context)
