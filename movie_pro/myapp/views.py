from django.shortcuts import render, redirect
from .forms import update1
from .models import Movie
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def adding(request):
    if request.method =="POST" and 'subm' in request.POST:
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    if request.method == "POST" and 'canc' in request.POST:
        return redirect('/')
    return render(request, "add.html")



def update(request,id):
    movie=Movie.objects.get(id=id)
    for1=update1(request.POST or None,request.FILES,instance=movie)
    if for1.is_valid():
        for1.save()
        return redirect('/')
    return render(request,'edit.html',{'form':for1,'movie':movie})

def delete(request,id):

    if request.method == "POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')