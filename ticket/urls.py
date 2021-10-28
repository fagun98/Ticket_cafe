from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    url('^$',views.index , name = 'index'),
    url(r'contact/',views.contact ,name ='contact'),
    url(r'Movies/',views.movies ,name ='movies'),
    url(r'Sports/',views.sports ,name ='sports'),
    url(r'Buy/',views.ticketentry,name ='buy'),
    url(r'BuyS/',views.sportsentry,name ='buy1'),
    url(r'BuyC/',views.concertentry,name ='buy2'),
    url(r'Sell/',views.sell ,name ='sell'),
    url(r'Login/',views.login ,name ='login'),
    url(r'SignUp/',views.signup ,name ='signup'),
    url(r'Search/$',views.search ,name ='search'),
    url(r'Search/(?P<id>\d+)/$',views.search ,name ='search'),
    url(r'Search2/$',views.search1 ,name ='search1'),
    url(r'Search2/(?P<id>\d+)/$',views.search1 ,name ='search1'),
    url(r'Search3/$',views.search2 ,name ='search2'),
    url(r'Search3/(?P<id>\d+)/$',views.search2 ,name ='search2'),
    url(r'^analysis/',views.graph ,name ='analysis'),
    url(r'^analysis2/',views.graph2 ,name ='analysis2'),
    url(r'^analysis4/',views.graphs ,name ='analysis4'),
    url(r'^analysis3/',views.graphm ,name ='analysis3'),
    url(r'^analysis5/',views.graphc ,name ='analysis5'),
    url(r'^logged/',views.logged ,name ='logged'),
    url(r'^sold/',views.sold ,name ='sold'),
    url(r'^concert/',views.concert ,name ='concert'),
    url(r'^successBought/',views.bought ,name ='bought'),
]
