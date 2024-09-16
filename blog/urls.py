from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
 path('', views.home_view, name='home'),
 path('blog/posts', views.post_list, name='blogs'),
 path('blog/tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
 path('blog/<int:id>/<slug:post>/', views.post_detail, name='post_detail'),
 path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
 path('post_message/', views.post_message, name='post_message'),
 path('blog/feed/', LatestPostsFeed(), name='post_feed'),
 path('blog/subscribe/', views.news_subscribe, name='news_subscribe'),
 
]