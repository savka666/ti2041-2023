from django.urls import path
from .views import post_list, post_detail, category_posts, tag_posts

app_name = 'blog'  

urlpatterns = [
    path('', post_list, name='post_list'),
    path('category/<int:category_id>/', category_posts, name='category_posts'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('tag/<int:tag_id>/', tag_posts, name='tag_posts'), 
]

