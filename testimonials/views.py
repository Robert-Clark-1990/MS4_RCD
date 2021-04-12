from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Testimonial
from .forms import TestimonialForm


def testimonials(request):
    """ A view to show the testimonials """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


def add_testimonial(request):
    """ Add a new testimonial to the page """
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial added successfully!')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to add testimonial.\
                 Please ensure the form is valid')
    else:
        form = TestimonialForm()

    form = TestimonialForm()
    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
