from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TeacherForm, StudentForm
from .models import Student, Teacher


# Create your views here.
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'users/student_list.html', {'students': students})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student.objects.all(), pk=pk)
    return render(request, 'users/student_detail.html', {'student': student})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'users/student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance=student)

    return render(request, 'users/student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'users/student_confirm_delete.html', {'student': student})

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'users/teacher_list.html', {'teachers': teachers})

@login_required
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher.objects.all(), pk=pk)
    return render(request, 'users/teacher_detail.html', {'teacher': teacher})

@login_required
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()

    return render(request, 'users/teacher_form.html', {'form': form})

@login_required
def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_detail', pk=pk)
    else:
        form = TeacherForm(instance=teacher)

    return render(request, 'users/teacher_form.html', {'form': form})

@login_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')

    return render(request, 'users/teacher_confirm_delete.html', {'teacher': teacher})