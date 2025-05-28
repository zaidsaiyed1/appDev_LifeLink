from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class UserRegisterationForm(UserCreationForm):
        email = forms.EmailField()
        class Meta:
                model=CustomUser
                fields = ('first_name','last_name','email','number','password1','password2','is_driver')


class UserRegisterationFormForOrganizerManager(UserCreationForm):
        email = forms.EmailField()
        class Meta:
                model=CustomUser
                fields = ('email','number','password1','password2','is_ambulanceOrganizer_Person')

class UserRegisterationFormForGovOfficial(UserCreationForm):
        email = forms.EmailField()
        class Meta:
                model=CustomUser
                fields = ('email','number','password1','password2','is_Gov_Official')
