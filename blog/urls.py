from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^blog$', views.blog, name='post_list'),
    url(r'^password$', views.password),
    url(r'^Secret-Area$', views.Secret_Area),
    url(r'^new_password$', views.password),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^Super-Secret-Area$', views.Super_Secret_Area),

]