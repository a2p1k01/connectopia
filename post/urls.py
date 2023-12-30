from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts_list, name='posts'),
    path('<int:year>/'
         '<int:month>/'
         '<int:day>/'
         '<slug:slug>/', views.post_detail, name='post_detail'),
    path('new_post', views.new_post, name='new_post'),
]

