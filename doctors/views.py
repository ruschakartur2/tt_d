from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from doctors.forms import DoctorCreationForm


class SignUpView(generic.CreateView):
    form_class = DoctorCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'