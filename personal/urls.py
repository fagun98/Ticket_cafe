from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    url('^$',views.index , name = 'index'),
    url(r'^contact/',views.cont, name='cont'),
    ]
