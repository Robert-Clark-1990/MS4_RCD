from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def management(request):
    """ A view to return the admin management page """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can access this page.')
        return redirect(reverse('home'))

    return render(request, 'management/management.html')
