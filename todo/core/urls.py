from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('addlist', views.addlist, name='addlist'),
    path('viewlist', views.viewlist, name='viewlist'),
    path('viewstats', views.viewstats, name='viewstats'),
    path('deletelist<str:pk>', views.deletelist, name='deletelist'),
]
