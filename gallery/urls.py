from django.urls import path, include
from gallery import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_prompt, name='upload_prompt'),
]
