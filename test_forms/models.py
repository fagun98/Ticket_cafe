from django.db import models
from django.urls import reverse

class Username(models.Model):
    uname = models.CharField(max_length=50,unique=True)
    upass = models.CharField(max_length=50)

    def __str__(self):
        return self.uname

    def get_absolute_url(self):
        return reverse('user-add', kwarg={'slug':self.slug})


    


