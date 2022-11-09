from django import forms
from .models import Contact


class ContactForms(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'date_of_birth')
