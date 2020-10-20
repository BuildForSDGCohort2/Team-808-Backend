from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:

        model = Patient
        fields = ('patient_names','dr_names','age','gender','test','result','file_image')

        widgets = {
        'patient_names': forms.TextInput(attrs={'class': 'form-control'}),
        'dr_names': forms.Select(attrs={'class': 'form-control'}),
        'age': forms.TextInput(attrs={'class': 'form-control'}),
        'gender': forms.TextInput(attrs={'class': 'form-control'}),
        'test': forms.TextInput(attrs={'class': 'form-control'}),
        'result': forms.Textarea(attrs={'class': 'form-control'}),
         }

class EditForm(forms.ModelForm):
    class Meta:

        model = Patient
        fields = ('patient_names','age','gender','test','result','file_image')

        widgets = {
        'patient_names': forms.TextInput(attrs={'class': 'form-control'}),
        
        'age': forms.TextInput(attrs={'class': 'form-control'}),
        'gender': forms.TextInput(attrs={'class': 'form-control'}),
        'test': forms.TextInput(attrs={'class': 'form-control'}),
        'result': forms.Textarea(attrs={'class': 'form-control'}),
         }