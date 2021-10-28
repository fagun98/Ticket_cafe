from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')
                  
def cont(request):
    return render(request, 'personal/basic.html',{'content' : ['Fuck you man','fuck@fuckyou.com']})
