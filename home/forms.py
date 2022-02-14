from django import forms
from django.core import validators
class FeedbackForm(forms.Form):
    name=forms.CharField(validators=[validators.MaxLengthValidator(20),validators.MinLengthValidator(5)])
    email=forms.EmailField(validators=[validators.EmailValidator()])
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(50),validators.MinLengthValidator(20)])

    # def clean_name(self):
    #     inputname=self.cleaned_data['name']
    #     if len(inputname)<5:
    #         raise forms.ValidationError('The minimum character should be 5')
    #     return inputname

    # def clean_email(self):
    #     inputemail=self.cleaned_data['email']
    #     if inputemail.endswith('@gmail.com'):
    #         return inputemail
    #     else:
    #         raise forms.ValidationError('Invalid Email')
    #
    # def clean_feedback(self):
    #     inputfeedback=self.cleaned_data['feedback']
    #     if len(inputfeedback)>50:
    #         raise forms.ValidationError('You can only enter maximum 50 characters')
    #     else:
    #         return inputfeedback







