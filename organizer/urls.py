from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # URLs para Tarefas
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/create/', views.task_create, name='task-create'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
    path('tasks/<int:pk>/update/', views.task_update, name='task-update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task-delete'),
    
    # URLs para Projetos
    path('projects/', views.project_list, name='project-list'),
    path('projects/create/', views.project_create, name='project-create'),
    path('projects/<int:pk>/', views.project_detail, name='project-detail'),
    path('projects/<int:pk>/update/', views.project_update, name='project-update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project-delete'),
]