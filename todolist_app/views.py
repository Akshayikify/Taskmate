from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from todolist_app.models import TodoList
from todolist_app.form import TaskList
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

App_name="Task Mate"
year=2018
@login_required
def todolist(request):
    if request.method=="POST":
        form=TaskList(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.owner=request.user
            instance.save()
            messages.success(request,("New Task is added"))
        return redirect('task')
    else:
        now=datetime.now()
        today=now.strftime('%B %d ,%Y')
        all_tasks=TodoList.objects.filter(owner=request.user).order_by('pk')
        paginator=Paginator(all_tasks,6)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        context={
            "App_name":App_name,
            "date":today,
            "All_tasks":all_tasks,
            }
        return render(request,'todolist_app/todolist.html',context)

#Method for contact section
def contact(request):
    context={
        "Heading":"Contact Us",
        "Content":"Start chat with our Team at any time."
    }
    return render(request,'todolist_app/contact.html',context)
#Method for about section
def about(request):
    context={
        "Heading":"About",
        "App_name": App_name,
        "Content":f"Established:{year} with ambition of providing the dynamic Todolist place for the user to create their own TodoList to make thier own better today.",
    }
    return render(request,'todolist_app/about.html',context)
@login_required
def delete_task(request,task_id):
    task=TodoList.objects.get(pk=task_id, owner=request.user)
    task.delete()
    return redirect('task')
@login_required
def edit_task(request,task_id):
    item = get_object_or_404(TodoList, pk=task_id,owner=request.user)
    if request.method=="POST":
        form=TaskList(request.POST or None,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,("Existing Task is updated"))
        return redirect('task')
    else:
        form=TaskList(instance=item)
        return render(request,'todolist_app/edit.html',{'form':form})
    
#Home/index page logic
def index(request):
    context={
        'App_name':App_name,
        'date': datetime.now()
    }
    return render(request,'todolist_app/index.html',context)