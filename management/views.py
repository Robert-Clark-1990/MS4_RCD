from django.shortcuts import render


def management(request):
    """ A view to return the admin management page """
    return render(request, 'management/management.html')
