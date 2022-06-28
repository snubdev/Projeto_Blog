from django.urls import path
from . import views
from .feeds import LatesPostsFeed
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    # views de postagens
    path('', views.post_list, name='post_list'),
    # ('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feed/', LatesPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')

]