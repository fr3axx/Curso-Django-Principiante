from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def tasks(request):
    # task = Task.objects.get(title=title)
    return render(request, 'tasks.html')