from django.urls import path
from . import views
urlpatterns = [
 
    path('newuser/registeration',views.newuser.as_view(),name='newuser' ),
    path('logout/',views.logout.as_view(),name='logout'),
    path('login/',views.login.as_view(),name='login'),
    path('forgotpassword/',views.forgotpassword.as_view(),name='forgotpassword'),
    path("check/for/recovery/<str:email>/",views.newpassword.as_view(),name='newpassword'),

    #for dashboard in views.dashboards

    path('dashboard/',views.dashboard.as_view(),name='profile'),


    #for editing userinformation
    path('editinfo/<int:id>/',views.editinfo.as_view(),name='editinfo'),
    path('editimage/<int:id>/',views.editimg.as_view(),name='editimage'),
    path('removeImage/<int:id>/',views.rmvimg.as_view(),name='rmvpic'),

]

