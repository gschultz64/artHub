from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<username>/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('forum/', views.forum, name='forum'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup')
]
