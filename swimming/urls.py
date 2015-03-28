from django.conf.urls import patterns, url

from swimming import views


urlpatterns = patterns(' ',
    url(r'^$', views.home, name='swimming_home'),
    url(r'^team/$', views.teamList, name='swimming_team_list'),
    url(r'^athlete/$', views.athleteList, name='swimming_athlete_list'),
    url(r'^team/(?P<pk>\d+)$', views.team, name='swimming_team'),
    url(r'^athlete/(?P<pk>\d+)$', views.athlete, name='swimming_athlete'),
)
