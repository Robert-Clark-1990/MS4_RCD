from checkout.models import Order

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, ImageUpload
from. forms import UserProfileForm, ImageUploadForm


@login_required
def profile(request):
    """
    Display the user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, 'Update failed.\
                 Please ensure the form is valid')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'Ths is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def image_upload(request):
    """
    Process images uploaded by the user
    """
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = get_object_or_404(UserProfile, user=request.user)
            image = form.cleaned_data.get("image")
            comments = form.cleaned_data.get("comments")
            ImageUpload.objects.create(user=user, image=image,
                                       comments=comments)
            messages.success(request, 'Image successfully uploaded!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Oops. Something went wrong. \
                Please try again.')
    return redirect(reverse('profile'))
