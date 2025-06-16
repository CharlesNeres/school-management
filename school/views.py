from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from school.forms import EnrollmentForm
from school.models import Enrollment


# Create your views here.
@login_required
def enrollment_list(request):
    enrollments = Enrollment.objects.select_related('student', 'course').all()
    return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})

@login_required
def enrollment_detail(request, pk):
    enrollment = get_object_or_404(Enrollment.objects.select_related('student', 'course'), pk=pk)
    return render(request, 'enrollments/enrollment_detail.html', {'enrollment': enrollment})

@login_required
def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()

    return render(request, 'enrollments/enrollment_form.html', {'form': form})

@login_required
def enrollment_update(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_detail', pk=pk)
    else:
        form = EnrollmentForm(instance=enrollment)

    return render(request, 'enrollments/enrollment_form.html', {'form': form})

@login_required
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')

    return render(request, 'enrollments/enrollment_confirm_delete.html', {'enrollment': enrollment})

