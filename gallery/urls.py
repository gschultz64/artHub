from django.urls import path
from django.conf.urls import url
from gallery import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<username>/', views.profile, name='profile'),
    path('user/<username>/upload/', views.upload, name='upload'),
    path('forum/', views.forum, name='forum'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update_profile, name='update'),
    path('basicupload/', views.BasicUploadView.as_view(), name='basic_upload')
]
