from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inquiry', views.inquiry, name='inquiry'),
]