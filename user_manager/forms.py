from django import forms
from django.forms import ModelForm,fields, models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    def v(self):
        #if(self[0] == 'a'):
        #   raise ValidationError("name should start with a")
        pass

    username = forms.CharField(validators=[v])
    password = forms.CharField(validators=[v])

class RegisterForm(ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('username','email','password')
