from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic import TemplateView

from django.urls import reverse_lazy

from pations.models import Patient


class HomePage(ListView):
    model = Patient
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class CreatePatiant(CreateView):
    model = Patient
    template_name = 'new_patient.html'
    fields = ['name', 'surname', 'adress', 'phonenumber', 'discrict', 'diagnos']
    success_url = reverse_lazy('home')


class PatientDetail(DetailView):
    model = Patient
    template_name = 'pation_detail.html'


class PatientEdit(UpdateView):
    model = Patient
    template_name = 'edit_patient.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class PatienDelete(DeleteView):
    model = Patient
    template_name = 'del_patient.html'
    success_url = reverse_lazy('home')
