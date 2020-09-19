
from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.forms.widgets import PasswordInput, TextInput
  
  
class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField() 
    # phone_no = forms.CharField(max_length = 20) 
    # first_name = forms.CharField(max_length = 20) 
    # last_name = forms.CharField(max_length = 20) 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] 
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password'}) 
