from django.conf.urls import url
from django.urls import path
from learn_app import views

app_name = "learn_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('reservation/', views.reservation, name='reservation'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),

]