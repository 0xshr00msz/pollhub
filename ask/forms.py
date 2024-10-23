from django import forms

class QuestionForm(forms.Form):
    # Arg 1: Value to be sent to the server
    # Arg 2: Value to be displayed to the user
    CHOICES = [('1', 'Yes'), ('2', 'No')]
    answer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)