from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Student
from studentorg.models import Organization
from studentorg.forms import StudentForm
from django.urls import reverse_lazy    


class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organizations'
    template_name = 'org_list.html'
    paginate_by = 5

class StudentList(ListView):
    model = Student 
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 10

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')
