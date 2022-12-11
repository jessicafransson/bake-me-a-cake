from . import views
from django.urls import path, include
from .views import PostList, PostLike, CreateRecipe, UpdateRecipe, DeleteRecipe


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='recipe_like'),
    path('create/', views.CreateRecipe.as_view(), name='create_recipe'),
    path(
        'update_recipe/<int:pk>', views.UpdateRecipe.as_view(),
        name='update_recipe'
        ),
    path(
        'delete_recipe/<int:recipe_id>',
        views.DeleteRecipe.as_view, name='delete_recipe'
        ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
