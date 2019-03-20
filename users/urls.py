from django.conf.urls import include, url
from .views import CreateUserAPIView

app_name = 'users'

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
]
