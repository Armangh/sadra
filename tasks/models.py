from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    employee = models.ManyToManyField("Employee")
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Status(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Employee(models.Model):
    MY_CHOICES = (
        ('stuff', 'Stuff'),
        ('admin', 'Admin'),
    )
    title = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=MY_CHOICES, default='stuff')

    def __str__(self):
        return self.user.username

class Replay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:20]