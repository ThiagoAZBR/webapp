from django.conf.urls import url, include
from users.views import HomePageView
 
urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^oauth/", include("social_django.urls")),
    url(r"^", HomePageView, name = 'home'),
    
]
