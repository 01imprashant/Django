from django import forms
from .models import project_variety

class project_variety_form(forms.Form):
    project_variety=forms.ModelChoiceField(queryset=project_variety.objects.all(),label='Select the project Variety')
 
