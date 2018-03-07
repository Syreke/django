from django.shortcuts import render

# Create your views here.

from .models import Teacher, Student

def index(request):
    num_students=Student.objects.all().count()
    num_teachers=Teacher.objects.count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
   
    return render(
        request,
        'index.html',
        context={'num_students':num_students,'num_teachers':num_teachers,'num_visits':num_visits},
    )
	
from django.views import generic

class StudentListView(generic.ListView):
    model = Student
    paginate_by = 3
class StudentDetailView(generic.DetailView):
    model = Student

class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 3
class TeacherDetailView(generic.DetailView):
    model = Teacher	