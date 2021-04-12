from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Testimonial
from .forms import TestimonialForm


def testimonials(request):
    """ A view to show the testimonials """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


@login_required
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


@login_required
def edit_testimonial(request, testimonial_id):
    """ Edit a testimonial """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    if request.method == 'POST':
        form = TestimonialForm(
            request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated testimonial!')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to update testimonial. \
                Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial)
        messages.info(request, f'You are editing {testimonial.name}')

    template = 'testimonials/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


@login_required
def delete_testimonial(request, testimonial_id):
    """Delete a testimonial """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted!')
    return redirect(reverse('management'))
