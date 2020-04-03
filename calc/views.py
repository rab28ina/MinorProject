from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html') 
def addcourse(request):
    return render(request,'AddCourse.html')   
def Teachers(request):
    if request.method == 'POST':
        teacherId=request.POST['teacherId']
        teacherName=request.POST['teacherName']
        teacherPhone=request.POST['teacherPhone']
        teacherEmailId=request.POST['teacherEmailId']
        
        if User.objects.filter(teacherId=teacherId).exists():
            messages.info(request,'Id already exits')
            return redirect('Teachers')
        elif User.objects.filter(teacherEmailId=teacherEmailId).exists():
            messages.info(request,'Email taken')
            return redirect('Teachers')
        else:
            user = User.objects.create_user(teacherId=teacherId,teacherName=teacherName,teacherPhone=teacherPhone,teacherEmailId=teacherEmailId)
            user.save();
            print('Teacher saved.')
            return redirect('Teachers')
    else:
        return render(request,'AddTeacher.html')  
def classroom(request):
    return render(request,'classroom.html')
def createtimetable(request):
    return render(request,'CreateTimeTable.html')  
