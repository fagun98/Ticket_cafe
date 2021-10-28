from django.contrib import admin

from ticket.models import ticketbuy,sportsbuy,concertbuy

admin.site.register(ticketbuy)
admin.site.register(sportsbuy)
admin.site.register(concertbuy)
