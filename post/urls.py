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
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('new_post/', views.new_post, name='new_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),

]

