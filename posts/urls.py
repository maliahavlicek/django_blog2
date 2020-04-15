from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post

from django.urls import path, include


urlpatterns = [
    path('', get_posts, name='get_posts'),
    path('?P<pk>/', post_detail, name='post_detail'),
    path('new/', create_or_edit_post, name='new_post'),
    path('?P<pk>/edit/', create_or_edit_post, name='edit_post')
]