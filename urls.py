from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fundbook.views.home', name='home'),
    # url(r'^fundbook/', include('fundbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	(r'^register/$','drinker.views.DrinkerRegistration'),
	(r'^login/$', 'drinker.views.LoginRequest'),
	(r'^logout/$','drinker.views.LogoutRequest'),    
     # homealone
	(r'^home/$','homealone.views.HomeAlone'),
     url(r'^blog/',include('blog.urls')),	
	
     #contact form
	(r'^contact/$', 'contactform.views.contactview'),
	 (r'^thankyou/$','contactform.views.thankyou'),
     #aboutus
	(r'^aboutus/$','contactform.views.aboutus'),
     #projects
	(r'^project/$','project.views.ProjectSubmit'),

)
