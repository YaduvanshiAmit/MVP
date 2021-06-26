from django import forms
from django.db.models import fields

from .models import EmailEntry

class EmailEntryForm(forms.ModelForm):
    class Meta:
        model = EmailEntry
        fields = ['email']

class EmailEntryUpdateForm(forms.ModelForm):
    class Meta:
        model = EmailEntry
        fields = ['email']



    def clean_email(self):
          # clean_field_name 
         email = self.cleaned_data.get("email")
         # if email.endswith('gmail.com'):
         #    raise forms.ValidationError
         # ("Invalid email")   

         qs = EmailEntry.objects.filter(email__iexact=email)

         if qs.exists():
             raise forms.ValidationError("Thankyou ,you have already register")
         return email




