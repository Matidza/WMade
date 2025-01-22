from django.conf.urls import handler404, handler500
from django.urls import path
from . import views

#handler404 = views.page_not_found
#handler500 = views.server_error

urlpatterns = [
    path('', views.index, name="index"), 
    path('my_view/', views.my_view, name='my_view')
]