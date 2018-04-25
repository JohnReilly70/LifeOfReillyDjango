from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'blog', views.blog, name='post_list'),
    url(r'password', views.password),
    url(r'Secret-Area', views.Secret_Area),
    url(r'new_password', views.password)
]