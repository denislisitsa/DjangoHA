from django.shortcuts import render
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teacher_list.html', context)

