from django.shortcuts import render

# Create your views here.

from tasks.models import Task


def get_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'index.html', {"tasks": tasks})
