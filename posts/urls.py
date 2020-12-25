from django.contrib import admin
from django.urls import include, path
import posts
from posts.views import post_create, post_delete, post_detail, post_filter_mixed_list, post_list, post_owned_list, post_update
from posts import views
from django.conf.urls import static, url
from django.conf import settings
import os
from django.views.static import serve
app_name="posts"
urlpatterns = [
    path('',  post_list.as_view(), name='post_list'),
    path('post/<int:pk>',  post_detail.as_view(), name='post_detail'),
    path('post_create',  post_create.as_view(), name='post_create'),
    path('post_delete/<int:pk>',  post_delete.as_view(), name='post_delete'),
    path('post_update/<int:pk>',  post_update.as_view(), name='post_update'),
    path('post_owned_list',  post_owned_list.as_view(), name='post_owned_list'),
    path('post_picture/<int:pk>', views.stream_file, name='post_picture'),
   # path('post_by_region',  post_by_region_list.as_view(), name='post_by_region_list'),
   # path('post_by_section',  post_by_section_list.as_view(), name='post_by_section_list'),
    path('post_by_section',  post_filter_mixed_list.as_view(), name='post_filter_mixed_list'),

] 


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]


urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]
