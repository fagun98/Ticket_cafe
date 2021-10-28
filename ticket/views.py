from django.shortcuts import render
from .models import ticketbuy,sportsbuy
import pygal
from pygal.style import DefaultStyle
from .filters import *
from .forms import *

#***************** HOME *****************
def index(request):
    return render(request, 'ticket/home1.html')

#***************** CONTACT *****************
def contact(request):
    return render(request, 'ticket/contact.html')

#***************** MOVIES *****************
def movies(request):
    return render(request, 'ticket/Movies.html')

#***************** SPORTS *****************
def sports(request):
    return render(request, 'ticket/Sports.html')

#***************** SOLD PAGE *****************
def sold(request):
    return render(request,'ticket/Sold.html')

#***************** ticket Selling is saved here // TB is class from .forms  *****************
def ticketentry(request):
    if request.method == 'POST':
        tick_buy = TB(request.POST);
        if tick_buy.is_valid:
           tick_buy.save();
        return render(request,'ticket/sold.html')

    if request.method=='GET':
        tick_buy = TB();
        return render(request,'ticket/ticketbuy_form.html',{'form':tick_buy})

#***************** Concert ticket selling is saved here in db // CB is class from .forms *****************
def concertentry(request):
    if request.method == 'POST':
        conc_buy = CB(request.POST);
        if conc_buy.is_valid:
           conc_buy.save();
        return render(request,'ticket/sold.html')

    if request.method=='GET':
        conc_buy = CB();
        return render(request,'ticket/concertbuy_form.html',{'form':conc_buy})

#***************** Sports ticket selling is saved here in db // SB is class from .forms *****************
def sportsentry(request):
    if request.method == 'POST':
        sport_buy = SB(request.POST);
        if sport_buy.is_valid:
            sport_buy.save();
        return render(request,'ticket/sold.html')

    if request.method=='GET':
        sport_buy = SB();
        return render(request,'ticket/sportsbuy_form.html',{'form':sport_buy})

#***************** bought page  *****************
def bought(request):
    return render(request,'ticket/bought.html')


#***************** this shows the ticket buying list from here and get deleted here // UserFilter is used from .filter *****************
def search(request,id=None):
    user_list=ticketbuy.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    if id:
        ticketbuy.objects.filter(pk=id)[0].delete()
        return render(request,'ticket/bought.html')
    
    return render(request,'ticket/user_list.html',{'filter':user_filter})


#***************** this displays the Sports buyinh list from here and get deleted here // SportsFilter is used from .filter *****************
def search1(request,id=None):
    user_list=sportsbuy.objects.all()
    user_filter = SportsFilter(request.GET, queryset=user_list)
    if id:
        sportsbuy.objects.filter(pk=id)[0].delete()
        return render(request,'ticket/bought.html')
    
    return render(request,'ticket/sports_list.html',{'filter':user_filter})

#***************** this display the Concert buyinh list from here and get deleted here // ConcFilter is used from .filter *****************
def search2(request,id=None):
    user_list=concertbuy.objects.all()
    user_filter = ConcFilter(request.GET, queryset=user_list)
    if id:
        concertbuy.objects.filter(pk=id)[0].delete()
        return render(request,'ticket/bought.html')
    
    return render(request,'ticket/concertlist.html',{'filter':user_filter})


#***************** Graph for TRENDING EVENTS // pygal is imported  *****************
def graph(request):
    tic_Count= ticketbuy.objects.all().count();
    movie_count= sportsbuy.objects.all().count();
    conc_count= concertbuy.objects.all().count();

    
    total_count = tic_Count + movie_count + conc_count;
    
    Movie_Count = (tic_Count/total_count)*100;
    sports_count = (movie_count/total_count)*100;
    concert_count = (conc_count/total_count)*100;  

    Movie_Count = round(Movie_Count,2)
    sports_count = round(sports_count,2)
    concert_count = round(concert_count,2)

    pie_chart = pygal.Pie(print_values=True, style=DefaultStyle(value_font_family='googlefont:Raleway',value_font_size=20,value_colors=()))

    pie_chart.title = 'Trending Event in (%)' 
    pie_chart.add('MOVIES', Movie_Count)
    pie_chart.add('SPORTS', sports_count)
    pie_chart.add('MUSIC CONCERTS',concert_count)
    pie_chart.render(is_unicode=True)

        
    context = {'pie':pie_chart.render(height=400)}

    return render(request,'ticket/graph.html',context=context)

#***************** Graph for TRENDING SPORTS // pygal is imported *****************
def graphs(request):

    sp_Count = sportsbuy.objects.filter(sportsname = 'OL').count();
    sp_Count1 = sportsbuy.objects.filter(sportsname = 'LA').count();
    sp_Count2 = sportsbuy.objects.filter(sportsname = 'IPL').count();
    sp_Count3 = sportsbuy.objects.filter(sportsname = 'NBA').count();
    sp_Count4 = sportsbuy.objects.filter(sportsname = 'PK').count();
    sp_Count5 = sportsbuy.objects.filter(sportsname = 'UFEA').count();

    total_count = sp_Count + sp_Count1 + sp_Count2 + sp_Count3 + sp_Count4 + sp_Count5;

    sp1 = (sp_Count/total_count)*100;
    sp2 = (sp_Count1/total_count)*100;
    sp3 = (sp_Count2/total_count)*100;
    sp4 = (sp_Count3/total_count)*100;
    sp5 = (sp_Count4/total_count)*100;
    sp6 = (sp_Count5/total_count)*100;

    sp1 = round(sp1,2);
    sp2 = round(sp2,2);
    sp3 = round(sp3,2);
    sp4 = round(sp4,2);
    sp5 = round(sp5,2);
    sp6 = round(sp6,2);
    
    pie_chart = pygal.Pie(print_values=True, style=DefaultStyle(value_font_family='googlefont:Raleway',value_font_size=20,value_colors=()))
    
    pie_chart.title = 'Sports Trending in 2018(in %)'
    pie_chart.add('LALGA', sp2)
    pie_chart.add('OLYMPICS',sp1)
    pie_chart.add('IPL',sp3)
    pie_chart.add('NBA',sp4)
    pie_chart.add('PRO-KHABBADI',sp5)
    pie_chart.add('UFEA',sp6)
    pie_chart.render(is_unicode=True)

    context = {'pie':pie_chart.render(height=400)}

    return render(request,'ticket/graph4.html',context=context)

#***************** Graph for  TRENDING THEATRE OF MOVIES  *****************
def graph2(request):
    tic_Count = ticketbuy.objects.filter(ttheatre = 'I').count();
    tic_Count1 = ticketbuy.objects.filter(ttheatre = 'P').count();
    tic_Count2 = ticketbuy.objects.filter(ttheatre = 'C').count();
    tic_Count3 = ticketbuy.objects.filter(ttheatre = 'PG').count();

    total_count = tic_Count + tic_Count1 +tic_Count2 +tic_Count3;

    tc1 = (tic_Count/total_count)*100;
    tc2 = (tic_Count1/total_count)*100;
    tc3 = (tic_Count2/total_count)*100;
    tc4 = (tic_Count3/total_count)*100;

    tc1 = round(tc1,2)
    tc2 = round(tc2,2)
    tc3 = round(tc3,2)
    tc4 = round(tc4,2)
    
    line_chart = pygal.HorizontalBar(print_values=True, style=DefaultStyle(value_font_family='googlefont:Raleway',value_font_size=20,value_colors=()))
    line_chart.title = 'Theatre Ratings in (%)'
    line_chart.add('INOX',tc1)
    line_chart.add('PVR', tc2)
    line_chart.add('City-Pride',tc3)
    line_chart.add('PVR GOLD',tc4)
    line_chart.render()
    context = {'line':line_chart.render(height=350)}

    return render(request,'ticket/graph2.html',context=context)

#***************** Graph for TRENDING CONCERTS EVENTS *****************

def graphc(request):
    conc_Count = concertbuy.objects.filter(concname = 'EDC').count();
    conc_Count1 = concertbuy.objects.filter(concname = 'MF').count();
    conc_Count2 = concertbuy.objects.filter(concname = 'SB').count();
    conc_Count3 = concertbuy.objects.filter(concname = 'GC').count();
    conc_Count4 = concertbuy.objects.filter(concname = 'SS').count();

    total_count = conc_Count + conc_Count1 + conc_Count2 + conc_Count3 + conc_Count4;

    cc1 = (conc_Count/total_count)*100;
    cc2 = (conc_Count1/total_count)*100;
    cc3 = (conc_Count2/total_count)*100;
    cc4 = (conc_Count3/total_count)*100;
    cc5 = (conc_Count4/total_count)*100;

    cc1 = round(cc1,2);
    cc2 = round(cc2,2);
    cc3 = round(cc3,2);
    cc4 = round(cc4,2);
    cc5 = round(cc5,2);
    
    line_chart = pygal.HorizontalBar(print_values=True, style=DefaultStyle(value_font_family='googlefont:Raleway',value_font_size=30,value_colors=()))
    line_chart.title = 'Concerts Ratings in (%)'
    line_chart.add('EDC',cc1)
    line_chart.add('MAGNETIC FIELD', cc2)
    line_chart.add('SUN BURN',cc3)
    line_chart.add('Super Sonic',cc5)
    line_chart.add('Global Citizen',cc4)
    line_chart.render()
    context = {'line':line_chart.render(height=350)}

    return render(request,'ticket/graph5.html',context=context)

#***************** Graph Trending movies  *****************
def graphm(request):
    
    tic_Count = ticketbuy.objects.filter(moviename = 'IM').count();
    tic_Count1 = ticketbuy.objects.filter(moviename = 'HCS').count();
    tic_Count2 = ticketbuy.objects.filter(moviename = 'TGF').count();
    tic_Count3 = ticketbuy.objects.filter(moviename = 'FF').count();
    tic_Count4 = ticketbuy.objects.filter(moviename = 'GG').count();
    tic_Count5 = ticketbuy.objects.filter(moviename = 'MI:F').count();
    tic_Count6 = ticketbuy.objects.filter(moviename = 'LO').count();
    tic_Count7 = ticketbuy.objects.filter(moviename = 'SW').count();
    tic_Count8 = ticketbuy.objects.filter(moviename = 'IN').count();

    total_count = tic_Count + tic_Count1 + tic_Count2 + tic_Count3 + tic_Count4 + tic_Count5 + tic_Count6 + tic_Count7 + tic_Count8;

    tc1 = (tic_Count/total_count)*100;
    tc2 = (tic_Count1/total_count)*100;
    tc3 = (tic_Count2/total_count)*100;
    tc4 = (tic_Count3/total_count)*100;
    tc5 = (tic_Count4/total_count)*100;
    tc6 = (tic_Count5/total_count)*100;
    tc7 = (tic_Count6/total_count)*100;
    tc8 = (tic_Count7/total_count)*100;
    tc9 = (tic_Count8/total_count)*100;

    tc1 = round(tc1,2);
    tc2 = round(tc2,2);
    tc3 = round(tc3,2);
    tc4 = round(tc4,2);
    tc5 = round(tc5,2);
    tc6 = round(tc6,2);
    tc7 = round(tc7,2);
    tc8 = round(tc8,2);
    tc9 = round(tc9,2);
    
    pie_chart = pygal.Pie(print_values=True, style=DefaultStyle(value_font_family='googlefont:Raleway',value_font_size=15,value_colors=()))
    pie_chart.title = 'Movies Trending in (%)'
    pie_chart.add('IromMan', tc1)
    pie_chart.add('Spiderman',tc2)
    pie_chart.add('GodFather', tc3)
    pie_chart.add('Fast Five', tc4)
    pie_chart.add('Gone Girl', tc5)
    pie_chart.add('MI:Fallout', tc6)
    pie_chart.add('Logan', tc7)
    pie_chart.add('StarWars', tc8)
    pie_chart.add('Inception', tc9)

    pie_chart.render(is_unicode=True)

    context = {'pie':pie_chart.render(height=400)}

    return render(request,'ticket/graph3.html',context=context)


#***************** LOGGED PAGE IS DISPLAYED *****************
def logged(request):
    return render(request,'ticket/logged.html')


#***************** CONCERT HOME *****************
def concert(request):
    return render(request,'ticket/Concerts.html')

#***************** THIS RETURNS BUYING PAFE OF TICKET *****************
def sell(request):
    queryset = ticketbuy.objects.all()
    context = {"tlist" : queryset}
    return render(request, 'ticket/sell.html',context)

#*****************LOGIN *****************
def login(request):
   return render(request, 'ticket/Login.html')

#***************** SIGNUP *****************
def signup(request):
    return render(request, 'ticket/signup.html')
