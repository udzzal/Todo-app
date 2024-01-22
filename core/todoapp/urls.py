from django.urls import path 
from .views import Todo_home,View_todo,Create_todo,Update_todo,Delete_todo,Login_user,logout_user,Register_view
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_POST


urlpatterns = [
    
    path('mylogin/',Login_user.as_view(),name='mylogin'),
    path('mylogout/',logout_user,name='mylogout'),
    path('register/',Register_view.as_view(),name='register'),
    
    path('',Todo_home.as_view() ,name='todo_home'),
    path('todo_details/<int:pk>/',View_todo.as_view(),name='todo_details'),
    path('create_todo',Create_todo.as_view(),name='create_todo'),
    path('todo_update/<int:pk>/',Update_todo.as_view(),name='todo_update'),
    path('todo_delete/<int:pk>/',Delete_todo.as_view(),name='todo_delete'),
    
]



