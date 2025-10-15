from django.shortcuts import render, redirect, get_object_or_404
from app1.forms import AddtaskForm
from app1.models import Addtask
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def addtask(request):
    if request.method=="POST":
        form_instance=AddtaskForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            t=data['task']
            d=data['date']
            s=Addtask.objects.create(user=request.user,task=t,deadline=d)
            s.save()
            return render(request,"addtask.html")
    if request.method=="GET":
        form_instance=AddtaskForm()
        context={'form':form_instance}
        return render(request,"addtask.html",context)

@login_required
def home(request):
    return render(request,"index.html")

@login_required
def viewtask(request):
    if request.method=='GET':
        tasks=Addtask.objects.filter(user=request.user)
        context={'tasks':tasks}
        return render(request,"viewtask.html",context)

@login_required
def donetask(request,task_id):
    if request.method=='POST':
        t=get_object_or_404(Addtask,id=task_id,user=request.user)
        t.done=True
        t.save()
        return redirect('app1:viewtask')

@login_required()
def deletetask(request,task_id):
    if request.method=='POST':
        t=get_object_or_404(Addtask,id=task_id,user=request.user)
        t.delete()
        return redirect('app1:viewtask')

@login_required
def filtertask(request):
    if request.method=='GET':
        selected_date=request.GET.get('date')
        tasks=[]
        if selected_date:
            tasks=Addtask.objects.filter(user=request.user,deadline=selected_date)

        context={'tasks':tasks,'selected_date':selected_date}
        return render(request,'viewtask.html',context)
