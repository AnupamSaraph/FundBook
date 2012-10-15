from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from drinker.forms import RegistrationForm , LoginForm
from drinker.models import Drinker
from django.contrib.auth import authenticate , login  , logout


def DrinkerRegistration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/login/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
			user.save()
			drinker= Drinker(user=user,name=form.cleaned_data['name'],register_date=form.cleaned_data['register_date'])
			drinker.save()
			return HttpResponseRedirect('/login/')
		else:
			return render_to_response('register.html',{'forms':form}, context_instance=RequestContext(request))

	else:
		'''user is not submitting the form, show them a blank registration form'''
		form = RegistrationForm()
		context = {'form': form}
		return render_to_response('register.html',context,context_instance=RequestContext(request))


def LoginRequest(request):
	if request.method == 'POST':
            form = LoginForm(request.POST)
	    username = request.POST['username']
            password = request.POST['password']
            drinker = authenticate(username=username, password=password)
            if drinker is not None:
		if drinker.is_active:
			login(request,drinker)
			return HttpResponseRedirect('/home/')
		else:
				print 'Your account is disable'
	    else:
			print 'Your username or password is incorrect'

	else:
		"""user is not submitting the form, show the login form"""
                form = LoginForm()
                context = {'form': form}
                return render_to_response('login.html', context, context_instance=RequestContext(request))



def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/register/')
