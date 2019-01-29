from django.shortcuts import render, redirect
from .models import Student
# 현재폴더 안의 models 파일의 Post를 import 한다

# Create your views here.

def index(request):
    student = Student.objects.all()
    return render(request, 'index.html', {'student':student})
    
def new(request):
    return render(request, 'new.html')
    
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    student = Student(name=name, email=email, birthday=birthday, age=age)
    student.save()
    
    return redirect(f'/student/{student.pk}')
    
def detail(request, student_id): # student의 id값을 넘겨 받는다
    student = Student.objects.get(pk=student_id)
    return render(request, 'detail.html', {'student': student})
    
def delete(request, student_id):
    # 삭제하는 코드
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/student/')
    
def edit(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'edit.html', {'student':student})
    
def update(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.birthday = request.POST.get('birthday')
    student.age = request.POST.get('age')
    student.save()
    
    return redirect(f'/student/{student.pk}/')