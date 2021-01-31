from django.conf.urls import url
from faleconosco.views import Formulario


urlpatterns = [   
    url(r"^fale_conosco/", Formulario.as_view(), name="fale_conosco"),
]