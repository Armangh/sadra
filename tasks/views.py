from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
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

    def get(self, request, **kwargs):
        self.object = self.get_object()
        notifications = self.object.notification_set.filter(
            Q(seen='unseen')
            & 
            Q(user=request.user)
        )
        print(notifications)
        for notification in notifications:
            notification.seen = 'seen'
            notification.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['form'] = ReplayForm
        context['replaies'] = models.Replay.objects.filter(task=self.kwargs['pk'])
        return context

class EmployeeDetailTasks(DetailView):
    model = models.Employee
    template_name = 'tasks/employee_task.html'

class UserTaskView(View):
    model = models.Task
    template_name = 'registration/profile.html'

    def get(self, request):
        try:
            tasks = self.model.objects.filter(Q(sender=request.user) | Q(assigners=request.user)).distinct()
            # tasks = self.model.objects.get(pk=request.user.id).task_set.all()
        except self.model.DoesNotExist:
            tasks = None
        return render(request, self.template_name, {'tasks': tasks})

class ReplayToTask(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Replay
    fields = ['text', 'task']

    def test_func(self):
        task = models.Task.objects.get(pk=self.request.POST['task'])
        return self.request.user in task.assigners.all() or self.request.user == task.sender

    def form_valid(self, form):
        form.instance.user = self.request.user
        task = models.Task.objects.get(pk=self.request.POST['task'])
        assigners = task.assigners.all()
        form.instance.task = task
        replay = form.save()
        notification = models.Notification.objects.create(task=task, verb='replay', replay=replay)
        for assigner in assigners:
            if self.request.user != assigner:
                notification.user.add(assigner)
            if self.request.user != task.sender:
                notification.user.add(task.sender.id)
        return super().form_valid(form)

class CreateTask(LoginRequiredMixin, CreateView):
    model = models.Task
    template_name = 'tasks/create.html'
    fields = ['title', 'description', 'assigners', 'status']

    def form_valid(self, form):
        form.instance.sender = self.request.user
        task = form.save()
        notification = models.Notification.objects.create(task=task, verb='task')
        for assigner in task.assigners.all():
            notification.user.add(assigner)

        return super().form_valid(form)


class InboxView(LoginRequiredMixin, View):
    model = models.Notification
    template_name = 'tasks/inbox.html'

    def get(self, request):
        try:
            notifications = self.model.objects.filter(user=self.request.user)
        except self.model.DoesNotExist:
            notifications = None
        return render(request, self.template_name, {'notifications': notifications})

def logout_view(request):
    logout(request)
    return redirect('login')
         