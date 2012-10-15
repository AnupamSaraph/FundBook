from django import forms
from django.forms.widgets import *

class ContactForm (forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=Textarea())
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)



