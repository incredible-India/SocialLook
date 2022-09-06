from django.urls import path
from . import views
urlpatterns = [
 
    path('newuser/registeration',views.newuser.as_view(),name='newuser' ),
    path('logout/',views.logout.as_view(),name='logout'),
    path('login/',views.login.as_view(),name='login'),
    path('forgotpassword/',views.forgotpassword.as_view(),name='forgotpassword'),
    path("check/for/recovery/<str:email>/",views.newpassword.as_view(),name='newpassword'),

    #for dashboard in views.dashboards

    path('dashboard/',views.dashboard.as_view(),name='profile')

]

