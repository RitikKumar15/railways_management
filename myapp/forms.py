from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TrainSearchForm(forms.Form):
  train_from = forms.CharField(label="Train From :", widget=forms.TextInput(attrs={'class':'form-control'}))
  train_to = forms.CharField(label="Train To :", widget=forms.TextInput(attrs={'class':'form-control'}))
  
class RegistrationForm(UserCreationForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
  class Meta:
    model = User
    fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
    labels = {'username': 'Username', 'first_name':'First Name', 'last_name':'Last Name'}
    widgets = {
      'username': forms.TextInput(attrs={'class':'form-control'}),
      'first_name': forms.TextInput(attrs={'class':'form-control'}),
      'last_name': forms.TextInput(attrs={'class':'form-control'}),
    }
    
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))