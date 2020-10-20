
from django.urls import path
from .views import HomeView, PatientDetailView,AddPatientView,AboutPageView,PatientsDetailsView,UpdatePatientView,DeletePatientView
from  django.conf import settings
from  django.conf.urls.static import static


urlpatterns = [
    
    path('', HomeView.as_view(), name= "home"),
    path('about/', AboutPageView.as_view(), name= "about"),
    path('allpatient/', PatientsDetailsView.as_view(), name= "allpatient"),

    path('patient/<int:pk>', PatientDetailView.as_view(), name="patient-detail"),
    path('add_patient/', AddPatientView.as_view(), name="add_patient"),
    path('patient/edit/<int:pk>', UpdatePatientView.as_view(), name="update_patient"),
    path('patient/<int:pk>/remove', DeletePatientView.as_view(), name="delete_patient")


]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
