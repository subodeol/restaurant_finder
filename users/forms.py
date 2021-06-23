from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('full_name',)
