from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def progress(self):
        tasks = self.task_set.all()
        if tasks.count() == 0:
            return 0
        done_tasks = tasks.filter(status='done').count()
        return int((done_tasks / tasks.count()) * 100)

class Task(models.Model):
    STATUS_CHOICES = [
        ('backlog', 'Backlog'),
        ('doing', 'Em Progresso'),
        ('done', 'Concluída'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='backlog')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
    
    def get_status_color(self):
        colors = {
            'backlog': 'secondary',
            'doing': 'warning',
            'done': 'success'
        }
        return colors.get(self.status, 'info')

