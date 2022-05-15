from django.urls import path
from homepage.forms import ContactForm1, ContactForm2
from homepage.views import ContactWizard
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('register/', ContactWizard.as_view([ContactForm1, ContactForm2])),

]