from django.contrib import admin
from .models import Task, Status, Employee, Replay, Notification

# Register your models here.

admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Employee)
admin.site.register(Replay)
admin.site.register(Notification)
