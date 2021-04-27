from django import forms


class FeedbackForm(forms.Form):
   name = forms.CharField(max_length=20)
   lastname = forms.CharField(max_length=20)
   age = forms.IntegerField(min_value=0, max_value=99)
   comment = forms.Textarea({'cols': '40', 'rows': '10'})