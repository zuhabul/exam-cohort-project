from django import forms

class questionForm(forms.Form):
    question = forms.CharField(max_length=300)
    option1 = forms.CharField(max_length=100)
    option2 = forms.CharField(max_length=100)
    option3 = forms.CharField(max_length=100)
    option4 = forms.CharField(max_length=100)
    answer = forms.CharField(max_length=100)
    
