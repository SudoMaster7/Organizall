from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Project
from .forms import TaskForm, ProjectForm

@login_required
def dashboard(request):
    tasks = Task.objects.filter(owner=request.user).order_by('-due_date')[:5]
    projects = Project.objects.filter(owner=request.user).order_by('-end_date')[:3]
    return render(request, 'organizer/dashboard.html', {
        'tasks': tasks,
        'projects': projects
    })

@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'organizer/tasks_pages/task_list.html', {'tasks': tasks})

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'organizer/projects_pages/project_list.html', {'projects': projects})

# Adicione aqui as views para create/update/delete
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Project
from .forms import TaskForm, ProjectForm

# ========== TASKS CRUD ==========
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'organizer/tasks_pages/task_form.html', {'form': form, 'title': 'Nova Tarefa'})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    return render(request, 'organizer/tasks_pages/task_detail.html', {'task': task})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('task-detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'organizer/tasks_pages/task_form.html', {'form': form, 'title': 'Editar Tarefa'})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('task-list')
    return render(request, 'organizer/tasks_pages/task_confirm_delete.html', {'task': task})

# ========== PROJECTS CRUD ==========
@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, 'Projeto criado com sucesso!')
            return redirect('project-list')
    else:
        form = ProjectForm()
    return render(request, 'organizer/projects_pages/project_form.html', {'form': form, 'title': 'Novo Projeto'})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = Task.objects.filter(project=project, owner=request.user)
    return render(request, 'organizer/projects_pages/project_detail.html', {
        'project': project,
        'tasks': tasks
    })

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('project-detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'organizer/projects_pages/project_form.html', {'form': form, 'title': 'Editar Projeto'})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('project-list')
    return render(request, 'organizer/projects_pages/project_confirm_delete.html', {'project': project})