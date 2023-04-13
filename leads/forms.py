"""
This module for forms in Django
"""

from django import forms
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = {
            'first_name',
            'last_name',
            'age',
            'agent',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'my-custom-class'})



class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {"username": UsernameField}
