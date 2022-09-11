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


    #delete this post from

    path('deletethispost/<int:id>/',views.deleteethispost.as_view(),name='deletethispost'),

    #for the showing all the post
    path('post/',views.post.as_view(),name='post'),

    #for the people posting

    path('people/',views.people.as_view(),name='people'),

    #showing the profile page and

    path('showprofile/<int:id>/',views.profile.as_view(),name='showprofile'),


    #follower,
    path('follow/<int:id>/',views.follow.as_view(),name='follow'),
    path('unfollow/<int:id>/',views.unfollow.as_view(),name='unfollow'),


    #see the follow list below

    path('followlist/',views.followlist.as_view(),name='followlist'),
    path('followerlist/',views.followerlist.as_view(),name='followerlist'),

    #post activity to

    path('post_activity/<int:id>/<int:uid>/',views.post_activity.as_view(),name='postact')

]

