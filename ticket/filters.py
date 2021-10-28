from django.contrib.auth.models import User
from .models import ticketbuy,sportsbuy,concertbuy
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = ticketbuy
        fields = ['tno','tdate','ttheatre','moviename']
        
class SportsFilter(django_filters.FilterSet):
    class Meta:
        model = sportsbuy
        fields = ['sno','sdate','sportsname']
   
  
class ConcFilter(django_filters.FilterSet):
    class Meta:
        model = concertbuy
        fields = ['cno','cdate','concname']
   
