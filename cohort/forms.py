from django import forms

class createCohortForm(forms.Form):
    name = forms.CharField(label='Cohort Name', max_length=100)

class addMemberForm(forms.Form):
    memberEmail = forms.CharField(label = 'Enter Email Address', max_length = 100)    

class addQuestionform(forms.Form):
    question = forms.CharField(max_length=200, label = 'Question')
    op1 = forms.CharField(max_length=200,label = 'Option 1')
    op2 = forms.CharField(max_length=200,label = 'Option 2')
    op3 = forms.CharField(max_length=200,label = 'Option 3')
    op4 = forms.CharField(max_length=200,label = 'Option 4')
    ans = forms.CharField(max_length=200,label = 'Answer')

class addExamForm(forms.Form):   
    CHOICES = (('Quiz','Quiz'),('Micro-Viva','Micro_Viva'),)  
    examName = forms.CharField(max_length=30, label= 'Enter Exam Name')
    examType = forms.ChoiceField(choices=CHOICES)