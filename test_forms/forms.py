from .models import Username
from django.core.files.storage import FileSystemStorage
from django import forms

class UC(forms.ModelForm):
    class Meta:
        model = Username
        fields = ['uname','upass']
    
