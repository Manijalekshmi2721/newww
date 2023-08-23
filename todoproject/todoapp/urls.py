from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Taskview.as_view(),name='cbvhome'),
    path('cbvupdate/<int:pk>/',views.update1.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
    path('cbvdetail/<int:pk>/',views.detail1.as_view(),name='cbvdetail'),
]