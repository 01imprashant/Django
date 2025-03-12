from django import forms
from .models import myapp_variety


class myapp_variety_form(forms.Form):
  app_variety = forms.ModelChoiceField(queryset=myapp_variety.objects.all(), label="Select App Variety")
  # app_variety = forms.CharField()