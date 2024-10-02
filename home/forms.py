



from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')

class LoginRegister(UserCreationForm):
    class Meta:
        model = Login_view
        fields = ('username', 'password1', 'password2')


class WorkerRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Worker
        fields = ('name', 'contact_no', 'email', 'address','type')


class CustomerRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Customers
        fields = ('name', 'contact_no', 'email', 'address')
 