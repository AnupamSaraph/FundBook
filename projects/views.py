from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from projects.forms import ProjectDetail
from projects.models import Project


def projectform(request):
	if request.method == 'POST':
		form = ProjectDetail(request.POST)
		if form.is_valid():
			project =  ProjectDetails(body=form.cleaned_data['body'] , email=form.cleaned_data['email'] , address=form.cleaned_data['address'])
			project.save()
			project1 = Project(title=title , start_date=form.cleaned_data['start_date'])
			project1.save()
			return HttpRedirectResponse('/hello/')
		else:
			return render_to_response('project.html',{'forms':form}, context_instance=RequestContext(request))

	else:
		form = (ProjectDetail)
		context = {'form': form}
		return render_to_response('project.html',context,context_instance=RequestContext(request))

