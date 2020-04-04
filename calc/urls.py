from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('AddCourse',views.AddCourse,name='AddCourse'),
    path('AddTeacher',views.AddTeacher,name='AddTeacher'),
    path('classroom',views.classroom,name='classroom'),
    path('CreateTimeTable',views.CreateTimeTable,name='CreateTimeTable')
   
]
