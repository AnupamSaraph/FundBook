#from django.http import HttpResponse 
#from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response , render
from contactform.forms import ContactForm
#from django.template import RequestContext , Context
#from django import forms
#from django.forms.widgets import *
#from django.core.mail import send_mail


def contactview(request):
	if request.method == 'POST':
		form = ContactForm (request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_Data['cc_myself']

			recipients = ['ashwini7security@gmail.com']
			if cc_myself:
				recipents.append(sender)

			from django.core.mail import send_mail
			send_mail(subject, message , sender , recipents)	
			return HttpResponseRedirect('/thankyou/')
	else:
	    form = ContactForm()
	
	return render(request,'contact.html', {'form': form,})



def thankyou (request):
	return render_to_response('thankyou.html')

def aboutus (request):
	return render_to_response('aboutus.html')
