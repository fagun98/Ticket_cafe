from django.db import models
from django.urls import reverse

class ticketbuy(models.Model):

    MOVIES = (
            ('IM','IRONMAN'),
            ('HCS','HOME COMING SPIDERMAN'),
            ('TGF','THE GODFATHER'),
            ('MI:F','MISSION IMPOSSIBLE FALLOUT'),
            ('FF','FAST-FIVE'),
            ('GG','GONE GIRL'),
            ('LO','LOGAN'),
            ('SW','STARWARS'),
            ('IN','INCEPTION'),
            )
    
    TTHEATRE = (
            ('I','INOX'),
            ('P','PVR'),
            ('C','CITY-PRIDE'),
            ('PG','PVR GOLD'),
        )
    moviename = models.CharField(max_length = 4 , choices = MOVIES)
    tdate = models.DateField()
    ttheatre = models.CharField(max_length = 3 , choices = TTHEATRE)
    tno = models.IntegerField()

    def __str__(self):
        return self.moviename

    #def get_absolute_url(self):
     #   return reverse('detail', kwarg={'slug':self.slug})

class sportsbuy(models.Model):

    SPORTS = (
                ('OL','OLYMPICS'),
                ('LA','LALIGA'),
                ('IPL','IPL'),
                ('NBA','NBA'),
                ('PK','PRO-KHABADDI'),
                ('UFEA','UFEA'),
                )
    
    sportsname = models.CharField(max_length = 4 , choices = SPORTS)
    sdate = models.DateField()
    sno = models.IntegerField()

    def __str__(self):
        return self.sportsname    

class concertbuy(models.Model):

    CONCNAME = (
                ('EDC','EDC'),
                ('MF','MAGNETIC FIELD'),
                ('SB','SUN BURN'),
                ('SS','SUPER SONIC'),
                ('GC','GLOBAL CITIZEN'),
                )
    
    concname = models.CharField(max_length = 4 , choices = CONCNAME)
    cdate = models.DateField()
    cno = models.IntegerField()

    def __str__(self):
        return self.concname    

