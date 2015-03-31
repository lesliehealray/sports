from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from swimming import views


urlpatterns = patterns(' ',
    url(r'^$', views.home, name='swimming_home'),
    url(r'^team/(?P<pk>\d+)$', views.team_detail, name='swimming_team_detail'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
