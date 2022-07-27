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
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # urls para alteração de senha
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # urls para reinicar a senha
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    path('suport/', views.suport, name='suport')



]