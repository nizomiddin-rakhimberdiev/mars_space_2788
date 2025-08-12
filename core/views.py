from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddStudentForm
from users.models import Student
import random

# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin = authenticate(username=username, password=password)
        if admin is not None:
            login(request, admin)
            return redirect('admin-page')
    return render(request, 'core/admin_login.html')

@login_required(login_url='admin-login')
def admin_view(request):
    students = Student.objects.all()
    return render(request, 'core/admin_view.html', {'students': students})

@login_required(login_url='admin-login')
def add_student_view(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            def check_student():
                username = str(random.randint(1000000, 9999999))
                password = str(random.randint(10000, 999999))
                user = authenticate(username=username, password=password)
                if user is None:
                    student.username = username
                    student.password = password
                    student.set_password(password)
                    student.save()
                    with open('students.txt', 'a') as f:
                        f.write(
                            f"{student.first_name}, {student.last_name}, SpaceID: {student.username} Parol:{password}, \n")
                    return redirect('admin-page')
                else:
                    return check_student()
            return check_student()

    else:
        form = AddStudentForm()
    return render(request, 'core/add_student.html', {'form': form})