from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Todo
from .forms import TodoModelForm, DeleteConfirmForm


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})


def new(request):
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo:index')

    return render(request, 'todo/new.html', {'form': form})


def show(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/show.html', {'todo': todo})


def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoModelForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo:show', pk)

    return render(request, 'todo/edit.html', {'form': form})


def delete(request, pk):
 #   if request.method != 'POST':
 #       return HttpResponseNotAllowed(['POST'])

 #   todo = get_object_or_404(Todo, pk=pk)
 #   todo.delete()
 #   return HttpResponse('success')
     form = DeleteConfirmForm(request.POST or None)
     if form.is_valid() and form.cleaned_data['check'] == True:
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return  redirect('todo:index')

     return render(request, 'todo/delete.html', {'form': form})

