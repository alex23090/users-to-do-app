from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ToDoList, ToDoItem
from .forms import ToDoListForm, ToDoItemForm


def HomePageView(request):
    if request.user.is_authenticated:
        return redirect('account')
    else:
        return redirect('login')
    return render(request, 'main.html')


@login_required(login_url='login')
def CreateListView(request):
    form = ToDoListForm(request.POST)
    profile = request.user.profile

    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.owner = profile
            todo_list.save()
            messages.success(request, 'To Do List was successfully created!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'todo_list_form.html', context)


@login_required(login_url='login')
def DeleteList(request, pk):
    profile = request.user.profile
    list = profile.todolist_set.get(id=pk)
    if request.method == 'POST':
        list.delete()
        messages.success(request, 'List was successfully deleted!')
        return redirect('account')
    context = {'object': list}
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def UpdateList(request, pk):
    profile = request.user.profile
    list = profile.todolist_set.get(id=pk)
    form = ToDoListForm(instance=list)

    if request.method == 'POST':
        form = ToDoListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            messages.success(request, 'List was successfully updated!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'todo_list_form.html', context)


@login_required(login_url='login')
def CreateItemView(request, pk):
    form = ToDoItemForm()
    list = ToDoList.objects.get(id=pk)

    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.todo_list = list
            todo_item.save()
            messages.success(request, 'To Do Item was successfully created!')
            return redirect('list', list.id)

    context = {'form': form}
    return render(request, 'todo_item_form.html', context)


def UpdateItem(request, pk):
    profile = request.user.profile
    item = ToDoItem.objects.get(id=pk)
    list = ToDoList.objects.get(id=item.todo_list.id)
    form = ToDoItemForm(instance=item)

    if request.method == 'POST':
        form = ToDoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item was successfully updated!')
            return redirect('list', list.id)

    context = {'form': form}
    return render(request, 'todo_item_form.html', context)


def DeleteItem(request, pk):
    item = ToDoItem.objects.get(id=pk)
    list = ToDoList.objects.get(id=item.todo_list.id)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item was successfully deleted!')
        return redirect('list', list.id)

    context = {'object': item}
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def ViewList(request, pk):
    list = ToDoList.objects.get(id=pk)
    list_items = ToDoItem.objects.all().filter(todo_list=pk)
    context = {'list_items': list_items, 'list': list}
    return render(request, 'list.html', context)