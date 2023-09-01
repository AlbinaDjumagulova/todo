from django.shortcuts import render, redirect

# Create your views here.

from tasks.models import Task


def get_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'index.html', {"tasks": tasks})


def get_list (request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request,'index.html',{"tasks": tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        create_at = request.POST.get('create_at')
        type = Task.objects.create(title=title, description=description, create_at=create_at, type=type)
        return redirect('index')
    return render(request,'index.html')


def update_task(request,id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('discription')
        create_at= request.POST.get('create_at')
        type= request.POST.get('type')
        task = Task.odjects.get(id=id)
        task.title=title
        task.description = description
        task.created_at = create_at
        task.type = type
        task.save()
        return redirect('index')
    return render(request,'Update.html')


def delete_task(request , id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('index')
    return  render (request, 'index.html')

