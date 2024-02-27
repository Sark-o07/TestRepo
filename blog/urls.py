from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('write/', views.write, name='blog-write'),
    path('search/', views.search, name='search'),
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='blog-post-delete'),
    path('category/<str:cats>/', views.category, name='blog-category'),
    path('latest_stories/', views.latest_posts, name='blog-latest-posts'),
]