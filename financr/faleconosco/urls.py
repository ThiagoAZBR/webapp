from django.conf.urls import url
from faleconosco.views import Formulario, fale_conosco, app_home, home_page,index
from django.urls import path

urlpatterns = [   
    url(r"^fale_conosco/", Formulario.as_view(), name="fale_conosco"),
    url(r'^faleconosco/', fale_conosco, name="faleconosco"),
    url(r'^app', app_home, name = 'app_home'),
    path('', home_page, name = 'home_page'),
    path('index/', index, name = 'index'),

    # path("", HomePageView.as_view(), name="home"),
    # path('app', AppScreenView.as_view(), name = 'app-screen')

]