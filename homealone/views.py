from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response



def HomeAlone(request):
	return render_to_response('home.html')
	
