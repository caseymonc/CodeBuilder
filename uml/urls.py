from django.conf.urls import patterns, url

from uml import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	

	#ex: /class/5/
	# Returns the class as JSON
	url(r'^class/new/$', views.RequestClass, name='RequestClass'),
	url(r'^class/(?P<class_id>\d+)/$', views.RequestClass, name='RequestClass'),

	#ex: /class/5/method
	# Returns all of the methods for a class as JSON
	url(r'^class/(?P<class_id>\d+)/method/$', views.RequestMethods, name='RequestMethods'),

	#ex: /class/5/method/10
	# Returns the method for a class as JSON
	url(r'^class/(?P<class_id>\d+)/method/new/$', views.RequestMethods, name='RequestMethods'),
	url(r'^class/(?P<class_id>\d+)/method/(?P<method_id>\d+)/$', views.RequestMethods, name='RequestMethods'),

	#ex: /class/5/member
	# Returns all of the members for a class as JSON
	url(r'^class/(?P<class_id>\d+)/member/new/$', views.RequestMembers, name='RequestMembers'),

	#ex: /class/5/member/11
	# Returns the memember for a class as JSON
	url(r'^class/(?P<class_id>\d+)/member/(?P<member_id>\d+)/$', views.RequestMembers, name='RequestMembers'),

	#ex: /interface/5/
	# Returns the interface as JSON
	url(r'^interface/new/$', views.RequestInterface, name='RequestInterface'),

	#ex: /interface/5/
	# Returns the interface as JSON
	url(r'^interface/(?P<interface_id>\d+)/$', views.RequestInterface, name='RequestInterface'),

	#ex: /class/5/method
	# Returns all of the methods for an interface as JSON
	url(r'^interface/(?P<interface_id>\d+)/method/$', views.RequestIMethods, name='RequestIMethods'),

	#ex: /class/5/method/10
	# Returns the method for an interface as JSON
	url(r'^interface/(?P<interface_id>\d+)/method/(?P<method_id>\d+)/$', views.RequestIMethod, name='RequestIMethod'),
)
