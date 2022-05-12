
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('birthday_notifier.urls', namespace='main')),
    path("users/", include("django.contrib.auth.urls")),
    path("users/", include('users.urls')),
    
]
