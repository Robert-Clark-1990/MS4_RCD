from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Project


def portfolio(request):
    """ A view to show the portfolio, including sorting and search queries """

    portfolio = Project.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No results found")
                return redirect(reverse('portfolio'))

            queries = Q(name__icontains=query) | Q(
                        para_1__icontains=query) | Q(
                        para_2__icontains=query) | Q(
                        para_3__icontains=query) | Q(
                        keywords__icontains=query)
            portfolio = portfolio.filter(queries)

    context = {
        'portfolio': portfolio,
        'search_term': query,
    }

    return render(request, 'portfolio/portfolio.html', context)


def project_detail(request, project_id):
    """ A view to individual portfolio project """

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'portfolio/project_detail.html', context)
