from django.urls import path

from . import views
urlpatterns = [
    path('', views.posts, name='posts'), #posts/
    path('create_post/', views.create_post, name='create_post'),
    path('detail_post/<int:pk>/', views.detail_post, name='detail_post'),
    path('update_post/', views.update_post, name='update_post'),
    path('delete_post/', views.delete_post, name='delete_post'),
]
