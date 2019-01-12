from django.urls import path

from .views import TaskListView, TaskDetailView, EmployeeDetailTasks, ReplayToTask

app_name = 'tasks'
urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('employee/<int:pk>/', EmployeeDetailTasks.as_view(), name='employee_task_detail'),
    path('submitreplay', ReplayToTask.as_view(), name='submit_replay'),
]
