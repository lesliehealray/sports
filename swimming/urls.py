from django.conf.urls import patterns, url

from swimming import views


urlpatterns = patterns(' ',
    url(r'^$', views.home, name='swimming_home'),
    url(r'^team/(?P<pk>\d+)$', views.team_detail, name='swimming_team_detail')
)
