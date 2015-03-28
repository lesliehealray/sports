from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from swimming.models import Team, Athlete


def home(request):
    context = {
        'team_count': Team.objects.count(),
        'athlete_count': Athlete.objects.count(),
    }
    return render(request, 'swimming/home.html', context)


def team(request, pk):
    team = get_object_or_404(Team, id=pk)
    return render(request, 'swimming/team.html', {'team': team})


def athlete(request, pk):
    athlete = get_object_or_404(Athlete, id=pk)
    return render(request, 'swimming/athlete.html', {'athlete': athlete})


def teamList(request):
    team_list = Team.objects.all()
    paginator = Paginator(team_list, 25)
    page = request.GET.get('page')
    try:
        teams = paginator.page(1)
    except PageNotAnInteger:
        teams = paginator.page(paginator.num_pages)
    return render(request, 'swimming/team_list.html', {'teams': teams})


def athleteList(request):
    athlete_list = Athlete.objects.all()
    paginator = Paginator(athlete_list, 25)
    page = request.Get.get('page')
    try:
        athletes = paginatro.page(page)
    except PageNotAnInteger:
        athletes = paginator.page(1)
    except EmptyPage:
        athletes = paginator.page(paginator.num_pages)
    return render(request, 'swimming/athlete_list.html', {'athlete': athletes})


# def  athlete
# github.com/calebsmith/j583-newschool/blob/add-pagination/roster/views.py
