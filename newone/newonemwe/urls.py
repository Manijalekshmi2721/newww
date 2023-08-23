from . import views
from django.urls import path

urlpatterns = [
    path('',views.resul,name='resul'),
    # path('ad/',views.adding,name='adding')
]