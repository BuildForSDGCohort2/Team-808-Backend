from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient
from .forms import PatientForm, EditForm
from django.urls import reverse_lazy

#def home(request):
   # return render(request, 'home.html',{})
 
class HomeView(ListView):
    model = Patient
    template_name = 'home.html'
    


class AboutPageView(ListView):
    model = Patient
    template_name = 'about.html'

class PatientsDetailsView(ListView):
    model = Patient
    template_name = 'allpatient.html'
    ordering = ['-id']

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient.html'

class AddPatientView(CreateView):
     model = Patient
     form_class = PatientForm
     template_name = 'add_patient.html'
     #fields = '__all__'


class UpdatePatientView(UpdateView):
    model = Patient
    form_class = EditForm
    template_name = 'update_patient.html'
    #fields = ['patient_names', 'age', 'gender', 'test', 'result', 'file_image']

class DeletePatientView(DeleteView):
    model = Patient
    template_name = 'delete.html'
    success_url = reverse_lazy('allpatient')