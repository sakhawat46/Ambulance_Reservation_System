from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Services(models.Model):
    services_title = models.CharField(max_length=255, verbose_name='Put Services Title')
    services_details = models.TextField(verbose_name='Services Content Write Here')
    services_image = models.ImageField(upload_to='services_images', verbose_name='Image', blank=True, null=True)

    def __str__(self):
        return str(self.services_title)



class Reservation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Enter Your Name')
    phone = models.CharField(max_length=255, verbose_name='Enter Your Phone Number')
    date = models.DateField(verbose_name='Enter Pickup Date')

    # rating = (
    # (1,"AC"),
    # (2,"NON AC"),
    # (2,"FREEZING"),
    # )


    # type_of_ambulance = models.IntegerField(choices=rating, verbose_name='Enter Ambulance Type')

    type_of_ambulance = models.ForeignKey(Services, on_delete=models.CASCADE)

    pickup_location = models.CharField(max_length=255, verbose_name='Enter Pickup Location')
    destination = models.CharField(max_length=255, verbose_name='Enter Destination')


    class Meta:
        ordering = ['date',]


    def __str__(self):
        return str(self.name)


class About(models.Model):
    at_a_glance = models.TextField()
    message_from_ceo = models.TextField()
    company_profile = models.TextField()
    our_concern = models.TextField()

    def __str__(self):
        return str(self.at_a_glance)


class Contract(models.Model):
    address = models.CharField(max_length = 250)
    phone = models.CharField(max_length = 250)
    mobile = models.CharField(max_length = 250)
    email = models.EmailField()

    def __str__(self):
        return str(self.mobile)


class Blog(models.Model):
    blog_title = models.CharField(max_length=255, verbose_name='Put a Title')
    blog_content = models.TextField(verbose_name='Blog Content Write Here')
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image', blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return str(self.blog_title)


# class Services(models.Model):
#     services_title = models.CharField(max_length=255, verbose_name='Put Services Title')
#     services_details = models.TextField(verbose_name='Services Content Write Here')
#     services_image = models.ImageField(upload_to='services_images', verbose_name='Image', blank=True, null=True)

#     def __str__(self):
#         return str(self.services_title)


class Logo(models.Model):
    logo_image = models.ImageField(upload_to='logo_images', verbose_name='Image', blank=True, null=True)
    

class Background(models.Model):
    first_background_title = models.CharField(max_length=255, default="")
    first_background_details = models.TextField(default="")
    first_background_image = models.ImageField(upload_to='background_image', blank=True, null=True)

    second_background_title = models.CharField(max_length=255, default="")
    second_background_details = models.TextField(default="")
    second_background_image = models.ImageField(upload_to='background_image', blank=True, null=True)

    third_background_title = models.CharField(max_length=255, default="")
    third_background_details = models.TextField(default="")
    third_background_image = models.ImageField(upload_to='background_image', blank=True, null=True)


class Home(models.Model):
    home_feature_image = models.ImageField(upload_to='home_images', verbose_name=' Home Feature Image', blank=True, null=True)