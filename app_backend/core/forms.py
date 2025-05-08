from django import forms
from .models import *

class Ambulancef(forms.ModelForm):
              class Meta:
                      model = ambulance
                      fields  = "__all__"