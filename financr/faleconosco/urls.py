from django.conf.urls import url
from faleconosco.views import Formulario, AppScreenView, HomePageView, fale_conosco


# alteração
from django.urls import path

urlpatterns = [   
    url(r"^fale_conosco/", Formulario.as_view(), name="fale_conosco"),
    url(r'^faleconosco/', fale_conosco, name="faleconosco"),

    path("", HomePageView.as_view(), name="home"),
    path('app', AppScreenView.as_view(), name = 'app-screen')

]