from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('AddCourse',views.addcourse,name='AddCourse'),
    path('AddTeacher',views.Teachers,name='AddTeacher'),
    path('classroom',views.classroom,name='classroom'),
    path('CreateTimeTable',views.createtimetable,name='CreateTimeTable')
   
]
