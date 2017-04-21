from django.conf.urls import url

from . import views

app_name = 'player'
urlpatterns = [
    url(r'meter/^$', views.get_meter, name='get_meter'),
]
