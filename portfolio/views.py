from django.shortcuts import render, get_object_or_404
from .models import Project


def portfolio(request):
    """ A view to show the portfolio, including sorting and search queries """

    portfolio = Project.objects.all()

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/portfolio.html', context)


def project_detail(request, project_id):
    """ A view to individual portfolio project """

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'portfolio/project_detail.html', context)
