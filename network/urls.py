from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),

    # post-related routes
    path('posts/create', views.create_post, name='create_post'),
    path('posts/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('following', views.friends_posts, name='following'),
    path('posts/<int:post_id>/like', views.like_post, name='like_post'),
    path('posts/<int:post_id>/unlike', views.unlike_post, name='unlike_post'),

    # user-related routes
    path('<str:username>', views.profile, name='profile'),
    path('<str:username>/follow', views.follow, name='follow'),
    path('<str:username>/unfollow', views.unfollow, name='unfollow'),
]
