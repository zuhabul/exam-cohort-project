from django import forms

class textForm(forms.Form):
    text = forms.CharField(max_length=50)