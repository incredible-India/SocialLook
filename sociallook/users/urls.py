from django.urls import path
from . import views
urlpatterns = [
 
    path('newuser/registeration',views.newuser.as_view(),name='newuser' ),
    path('logout/',views.logout.as_view(),name='logout'),
    path('login/',views.login.as_view(),name='login')
]

