from django.urls import path
from . import views
from blog.views import BlogHome


urlpatterns = [
    path('', BlogHome.as_view(), name='blog-home'),
    path('about/', views.about,name='blog-about'),
]
