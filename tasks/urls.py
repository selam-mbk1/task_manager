from django.urls import path
from . import views

urlpatterns = [
    path('task_list/', views.task_list_view, name='task_list'),
    path('task/create/', views.task_create_view, name='task_create'),
    path('task/<int:pk>/toggle/', views.task_toggle_view, name='task_toggle'),
    path('task/<int:pk>/update/', views.task_update_view, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete_view, name='task_delete'),
    path('task/<int:pk>/complete/', views.task_complete_view, name='task_complete'),
    path('task/<int:pk>/incomplete/', views.task_incomplete_view, name='task_incomplete'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
