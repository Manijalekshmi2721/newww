from pickle import GET

from django.http import HttpResponse
from django.shortcuts import render

from .models import Place, Person


# Create your views here.
def resul(request):
    obj= Place.objects.all()
    ob=Person.objects.all()
    return render(request,"index.html",{'result':obj,'hi':ob})
# def adding(request):
#     x=int(request.GET['a'])
#     y=int(request.GET['b'])
#     d1=x+y
#     d2=x-y
#     d3=x*y
#     d4=x/y
#     return render(request,"result.html",{'s':d1,'s1':d2,'s2':d3,'s3':d4})