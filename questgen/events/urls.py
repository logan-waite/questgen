from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.EventList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
