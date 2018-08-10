from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gallery import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<username>/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('forum/', views.forum, name='forum'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update_profile, name='update'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
