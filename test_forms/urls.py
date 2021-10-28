from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
        url('^$',views.userindex , name = 'userindex'),
        url(r'test/add$',views.UserCreate,name='user-add'),
    ]
