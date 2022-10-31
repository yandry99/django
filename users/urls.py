# -*- coding: utf-8 -*-
from django.urls import path

from . import views
urlpatterns = [
   
    #===============Persona
    path('', views.PersonaList.as_view(), name='persona_list'),    
    path('view/<int:pk>', views.PersonaDetail.as_view(), name='persona_view'),
    path('new', views.PersonaCreate.as_view(), name='persona_new'),
    path('edit/<int:pk>', views.PersonaUpdate.as_view(), name='persona_edit'),
    path('delete/<int:pk>', views.PersonaDelete.as_view(), name='persona_delete'),
]