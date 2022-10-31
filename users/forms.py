# -*- coding: utf-8 -*-
from django import forms

from .models import Persona

class PersonaForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(PersonaForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs = {
    #         'class': 'form-control col-md-6'
    #     }
    #     self.fields['description'].widget.attrs = {
    #         'class': 'form-control col-md-6'
    #     }
    #     self.fields['price'].widget.attrs = {
    #         'class': 'form-control col-md-6',
    #         'step': 'any',
    #         'min': '1',
    #     }

    class Meta:
        model = Persona
        fields = "__all__"