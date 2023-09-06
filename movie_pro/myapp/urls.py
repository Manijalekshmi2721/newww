from . import views
from django.urls import path
app_name='myapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movies/<int:movie_id>/',views.detail,name='detail'),
path('adding/',views.adding,name='adding'),
path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')]
