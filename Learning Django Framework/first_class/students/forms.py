from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','age','profile_pic','dob']
        
        labels ={
            'name' :'Full Name',
            'email':'Email Address',
            'Age':'Age',
            'profile_pic':'profile_pic',
        }
        
       # Adding custom widgets for better UI
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'age': forms.NumberInput(attrs={'class': 'form-control'}),
        'dob': forms.DateInput(
         attrs={'type': 'date', 'class': 'form-control'}
        ),
        }