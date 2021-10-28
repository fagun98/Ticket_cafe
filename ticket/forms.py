from .models import ticketbuy,sportsbuy,concertbuy
from django.core.files.storage import FileSystemStorage
from django import forms

class TB(forms.ModelForm):
    class Meta:
        model = ticketbuy
        fields = ['tdate','ttheatre','tno','moviename']

class SB(forms.ModelForm):
    class Meta:
        model = sportsbuy
        fields = ['sportsname','sdate','sno']

class CB(forms.ModelForm):
    class Meta:
        model = concertbuy
        fields = ['concname','cdate','cno']
