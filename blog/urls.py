<<<<<<< HEAD
from django.urls import path
from . import views
from blog.views import BlogHome


urlpatterns = [
    path('', BlogHome.as_view(), name='blog-home'),
    path('about/', views.about,name='blog-about'),
]
=======
from django.urls import path
from . import views
from blog.views import BlogHome


urlpatterns = [
    path('', BlogHome.as_view(), name='blog-home'),
    path('about/', views.about,name='blog-about'),
]
>>>>>>> 6463235276beeb7b320d35990b989260ea8036c4
