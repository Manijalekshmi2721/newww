from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

from .forms import form1
from .models import Todoclass


# Create your views here.
def home(request):
    task=Todoclass.objects.all()
    if request.method=="POST":
        name=request.POST.get('name','')
        pr = request.POST.get('priority', '')
        date=request.POST.get('date','')
        task=Todoclass(name=name,priority=pr,date=date)
        task.save()
    return render(request,'home.html',{'task':task})


class Taskview(ListView):
    model = Todoclass
    template_name = 'home.html'
    context_object_name = 'task'

class TaskDeleteView(DeleteView):
    model = Todoclass
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

class detail1(DetailView):
    model = Todoclass
    template_name = 'detail.html'
    context_object_name = 'task'
class update1(UpdateView):
    model = Todoclass
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name', 'priority', 'date']
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


def update(request,id):
    task=Todoclass.objects.get(id=id)
    form=form1(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})

def delete(request,taskid):
    task = Todoclass.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')