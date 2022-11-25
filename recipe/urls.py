from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create/', views.CreatePost.as_view(), name='create_post'),
    path('update/<slug:slug>/', views.UpdatePost.as_view(), name='update_post'),
    path('delete/<slug:slug>/', views.DeletePost.as_view(), name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
