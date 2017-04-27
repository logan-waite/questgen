from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "game"
urlpatterns = [
    url(r'^$', views.GameList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
