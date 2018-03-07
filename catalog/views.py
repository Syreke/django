from django.shortcuts import render

# Create your views here.

from .models import Teacher, Student

def index(request):
    num_students=Student.objects.all().count()
    num_teachers=Teacher.objects.count()
    
   
    return render(
        request,
        'index.html',
        context={'num_students':num_students,'num_teachers':num_teachers},
    )
	
from django.views import generic

class StudentListView(generic.ListView):
    model = Student
    paginate_by = 2
class StudentDetailView(generic.DetailView):
    model = Student