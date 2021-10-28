from django.urls import path, include
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import RePost

urlpatterns = [

url(r'^$', ListView.as_view(queryset=RePost.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),

 url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = RePost,
                                    template_name="blog/post.html")),
]
