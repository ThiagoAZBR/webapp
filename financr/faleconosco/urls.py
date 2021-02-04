from django.conf.urls import url
from faleconosco.views import Formulario
from faleconosco.views import HomePageView, AppScreenView, TransactionScreenView

# alteração
from django.urls import path

urlpatterns = [   
    url(r"^fale_conosco/", Formulario.as_view(), name="fale_conosco"),


    path("", HomePageView.as_view(), name="home"),
    path('app', AppScreenView.as_view(), name = 'app-screen'),
    path('transactions', TransactionScreenView.as_view(), name = 'transaction-screen'),

]