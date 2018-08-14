from django.urls import path
from django.conf.urls import url
from gallery import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<username>/', views.profile, name='profile'),
    path('user/<username>/upload/', views.upload, name='upload'),
    path('chat/', views.chat, name='chat'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:media_id>/', views.show, name='show'),
]
