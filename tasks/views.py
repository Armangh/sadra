from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from . import models

# Create your views here.

class TaskListView(ListView):
    model = models.Task
    template_name = "tasks/task_list.html"

class TaskDetailView(DetailView):
    model = models.Task
    template_name = 'tasks/task_detail.html'
    query_set = models.Task.objects.all().prefetch_related('Employee')

class EmployeeDetailTasks(DetailView):
    model = models.Employee
    template_name = 'tasks/employee_task.html'

class UserTaskView(View):
    model = models.Employee
    template_name = 'registration/profile.html'

    def get(self, request):
        try:
            tasks = self.model.objects.get(pk=request.user.id).task_set.all()
        except self.model.DoesNotExist:
            tasks = None
        return render(request, self.template_name, {'tasks': tasks})

def logout_view(request):
    logout(request)
    return redirect('login')
         