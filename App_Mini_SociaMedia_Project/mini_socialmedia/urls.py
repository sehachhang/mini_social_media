from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
