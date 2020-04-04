from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('Teachers',views.Teachers,name='Teachers'),
    path('classroom',views.classroom,name='classroom'),
    path('createtimetable',views.createtimetable,name='createtimetable')
   
]
