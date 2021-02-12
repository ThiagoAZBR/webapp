from django.conf.urls import url, include
from django.urls import path
 
urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
]
