from django.shortcuts import render, get_object_or_404
from swimming.models import Team


def home(request):
    context = {
        'teams': Team.objects.all(),
    }
    return render(request, 'swimming/home.html', context)


def team_detail(request, pk):
    team = get_object_or_404(Team, id=pk)
    return render(request, 'swimming/team_detail.html', {'team': team})
