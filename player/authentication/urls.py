from django.conf.urls import url
from .views import sign, register

urlpatterns = [
    url(r'^auth/', register, name="index"),
]