from django.conf.urls import url
from faleconosco.views import Formulario, fale_conosco, app_home, HomePageView
from django.urls import path
from users.views import Functions, RegisterPage
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [   
    url(r"^fale_conosco/", Formulario.as_view(), name="fale_conosco"),
    url(r'^faleconosco/', fale_conosco, name="faleconosco"),
    url(r'^app', app_home, name = 'app_home'),
    url(r'^', RegisterPage, name="home")

]