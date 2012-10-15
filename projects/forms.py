from django import forms 
from django.forms.widgets import *
from projects.models import Project
from django.forms import ModelForm

class ProjectDetails (ModelForm):
	body = forms.CharField(widget=Textarea())
	email = forms.EmailField()
	address = forms.charField(widget=Textarea())
	

	class Meta:
		model = Projects
		exclude = ('title',)
	
	
