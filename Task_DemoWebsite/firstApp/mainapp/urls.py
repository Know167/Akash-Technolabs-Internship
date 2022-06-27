from importlib.resources import path
from django.urls import URLPattern, path
from . import views

urlpatterns=[
    
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('github',views.github, name='github'),
    path('linkedin',views.linkedin, name='linkedin'),
    path('insta',views.insta, name='insta')
    ]
                                                    