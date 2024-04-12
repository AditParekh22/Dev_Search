from django.urls import path
from . import views

urlpatterns = [
    path('', views.project1, name="project1"),
    path('project/<str:pk>/', views.project2, name="project2"),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),
]
