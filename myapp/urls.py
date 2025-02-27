from django.urls import path
from .views import *
from . import views

app_name = 'myapp'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', loginu, name='login'),
    path('logout/', ulogout, name='logout'),
    path('account_details/', views.account_details, name='account_details'),
    path('modify_account/', views.modify_account, name='modify_account'),
    path('author_dashboard/', author_dashboard, name='author_dashboard'),
    path('author_list/', author_list, name='author_list'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('blog/add/', views.blog_add, name='blog_add'),
    path('blog/edit/<int:id>/', views.blog_edit, name='blog_edit'),
    path('blog/delete/<int:id>/', views.blog_delete, name='blog_delete'),
    # path('author/add/', views.add_blog, name='add_blog'),
    # path('author/alter/', views.alter_blog, name='alter_blog'),
    # path('author/delete/', views.delete_blog, name='delete_blog'),    
]
