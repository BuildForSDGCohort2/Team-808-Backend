from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Patient(models.Model):
    patient_names = models.CharField(max_length=255)
    dr_names = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    test = models.CharField(max_length=255)
    result = models.TextField()
    file_image = models.ImageField(null=True, blank=True, upload_to='images/')
    

    def __str__(self):
        return self.patient_names  + ' | ' + str(self.dr_names)

    def get_absolute_url(self): 
        return reverse('allpatient')