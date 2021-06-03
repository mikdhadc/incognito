from django import forms
from django.forms import ModelForm,fields, models
from .models import Message

class MsgForm(ModelForm):
    def v(self):
        return 'not valid'

    name = forms.CharField(max_length=10, validators=[v], required=False)

    class Meta:
        model = Message
        fields = '__all__'