from datetime import date
from django.shortcuts import render,redirect
from .models import Student,Course
from .forms import *

def index(request):
    students = Student.objects.all()
    return render(request, 'djangoKeys2APP/index.html',{'students': students})

def create(request):
    initilizate()
    if request.method == "POST":
        student = Student()
        student.name = request.POST.get("name")
        course_ids = request.POST.getlist("courses")
        student.save()
        courses = Course.objects.filter(id__in=course_ids)
        student.courses.set(courses, through_defaults={"date": date.today(), "mark": 0})
        return redirect("index")
    courses = Course.objects.all()
    return render(request, "djangoKeys2APP/create.html",{"courses":courses})


def initilizate():
    if Course.objects.all().count() == 0:
        Course.objects.create(name="Python")
        Course.objects.create(name="Django")
        Course.objects.create(name="FastAPI")
