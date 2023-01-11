from django.forms import ModelForm
from .models import Account

from django.contrib.auth.forms import UserCreationForm

#forms
class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email','password1','password2','phone_number','first_name','last_name')