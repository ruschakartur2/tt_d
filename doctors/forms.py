from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Doctor
from django.contrib.auth.models import User



class DoctorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Doctor
        fields = UserCreationForm.Meta.fields + ('docSpec','spec')
