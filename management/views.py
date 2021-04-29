from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from profiles.models import ImageUpload


@login_required
def management(request):
    """ A view to return the admin management page """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can access this page.')
        return redirect(reverse('home'))

    return render(request, 'management/management.html')


@login_required
def order_history(request):
    """ A view to return all customer order history """
    orders = Order.objects.all().order_by('-date')

    template = 'management/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def view_uploads(request):
    """ A view to return all images uploaded by customers """
    uploads = ImageUpload.objects.all()

    template = 'management/view_uploads.html'
    context = {
        'uploads': uploads,
    }

    return render(request, template, context)
