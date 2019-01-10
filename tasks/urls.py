from django.urls import path

from .views import TaskListView, TaskDetailView, EmployeeDetailTasks

app_name = 'tasks'
urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('employee/<int:pk>/', EmployeeDetailTasks.as_view(), name='employee_task_detail'),
]
