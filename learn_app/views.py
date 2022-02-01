from unicodedata import name
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from learn_app.forms import ReservationForm
from learn_app.models import Reservation, About, Contract, Blog, Services, Logo, Background, Home
from django.core.mail import send_mail

# Create your views here.

def home(request):

    logo_information = Logo.objects.order_by('logo_image')
    background_information = Background.objects.order_by('first_background_title')
    home_feature = Home.objects.order_by('home_feature_image')

    diction ={'title':'Home Page', 'logo_information': logo_information, 'background_information': background_information, 'home_feature': home_feature}
    return render(request,'learn_app/home.html', context = diction)

def about(request):

    logo_information = Logo.objects.order_by('logo_image')
    about_information = About.objects.order_by('at_a_glance')
    background_information = Background.objects.order_by('first_background_title')

    diction ={'title':'About Page', 'about_information': about_information, 'logo_information': logo_information, 'background_information': background_information}
    return render(request,'learn_app/about.html', context = diction)

def services(request):

    logo_information = Logo.objects.order_by('logo_image')
    services_information = Services.objects.order_by('services_title')
    background_information = Background.objects.order_by('first_background_title')

    diction ={'title':'Services Page', 'services_information': services_information, 'logo_information': logo_information, 'background_information': background_information}
    return render(request,'learn_app/services.html', context = diction)




def reservation(request):
    logo_information = Logo.objects.order_by('logo_image')
    background_information = Background.objects.order_by('first_background_title')
    form = ReservationForm()
    registered = False
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            return HttpResponseRedirect(reverse('learn_app:home'))
    diction ={'title':'Reservation Page', 'form':form, 'registered':registered, 'logo_information': logo_information, 'background_information': background_information}
    return render(request,'learn_app/reservation.html', context = diction)





def blog(request):

    logo_information = Logo.objects.order_by('logo_image')
    blog_details = Blog.objects.order_by('blog_title')
    background_information = Background.objects.order_by('first_background_title')

    diction ={'title':'Blog Page', 'blog_details': blog_details, 'logo_information': logo_information, 'background_information': background_information}
    return render(request,'learn_app/blog.html', context = diction)

def contact(request):

    logo_information = Logo.objects.order_by('logo_image')
    contact_details = Contract.objects.order_by('mobile')
    background_information = Background.objects.order_by('first_background_title')

    diction ={'title':'Contact Page', 'contact_details': contact_details, 'logo_information': logo_information, 'background_information': background_information}
    return render(request,'learn_app/contact.html', context = diction)

    