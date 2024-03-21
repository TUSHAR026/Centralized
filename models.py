
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.IntegerField()
    assigned_team_members = models.ManyToManyField(User, related_name='assigned_tasks')

    def __str__(self):
        return self.title
