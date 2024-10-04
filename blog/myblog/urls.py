
from django.urls import path
from .views import *

app_name = 'myblog'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('about/', about, name='about'),
    path('index_blog/', index_blog, name='index_blog'),
    path('send_data/', send_data, name='send_data'),
    path('add_post/', add_post, name='add_post'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
]


