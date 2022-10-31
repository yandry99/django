from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Persona
from .forms import PersonaForm

#===========================================Personas
class PersonaList(ListView): 
    
       model = Persona
    
class PersonaDetail(DetailView): 
    model = Persona
    
class PersonaCreate(SuccessMessageMixin, CreateView): 
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('persona_list')
    success_message = "Product successfully created!"
    
class PersonaUpdate(SuccessMessageMixin, UpdateView): 
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('persona_list')
    success_message = "Persona successfully updated!"

class PersonaDelete(SuccessMessageMixin, DeleteView):
    model = Persona
    success_url = reverse_lazy('persona_list')
    success_message = "Persona successfully deleted!"