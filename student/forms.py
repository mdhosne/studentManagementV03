from django.forms import forms
from . import models
class StudentForm(forms.ModelForm):
    class Meta:
        labels = {
            'name': 'Full Name',
            'photo': 'Upload Photo'
        }
        help_texts = {
            'email': 'Email will be confidential',
            
        }
