from django.contrib import admin
from django.urls import re_path
from ifphotos import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^info/$', views.InfoView.as_view(), name='info'),
    # re_path(r'^admin/', admin.site.urls),
]
