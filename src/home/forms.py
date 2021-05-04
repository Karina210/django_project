from django import forms
from home.models import Customer

# class FeedbackForm(forms.Form):
#    name = forms.CharField(max_length=20)
#    lastname = forms.CharField(max_length=20)
#    age = forms.IntegerField(min_value=0, max_value=99)
#    comment = forms.Textarea({'cols': '40', 'rows': '10'})


class CustomerForm(forms.ModelForm):
   class Meta:
      model = Customer
      fields = ['firstname', 'lastname', 'age']

