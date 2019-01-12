from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models
from .forms import ReplayForm

# Create your views here.

class TaskListView(ListView):
    model = models.Task
    template_name = "tasks/task_list.html"

class TaskDetailView(DetailView):
    model = models.Task
    template_name = 'tasks/task_detail.html'
    query_set = models.Task.objects.all().prefetch_related('Employee')

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['form'] = ReplayForm
        context['replaies'] = models.Replay.objects.filter(task=self.kwargs['pk'])
        return context

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

class ReplayToTask(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Replay
    fields = ['text', 'task']

    def test_func(self):
        obj = self.get_object()
        return self.request.user in obj.task.employee.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        task = models.Task.objects.get(pk=self.request.POST['task'])
        form.instance.task = task
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect('login')
         