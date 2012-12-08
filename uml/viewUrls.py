from django.conf.urls import patterns, url
from uml import renderView


urlpatterns = patterns('',
	

	#ex: /class/5/
	# Returns the class as JSON
	url(r'^$', renderView.index, name='index'),

	#ex: /class/new/
	# Returns the class as JSON
	url(r'^login/login/$', renderView.Login, name='Login'),
	url(r'^login/register/$', renderView.Register, name='Register'),

	#ex: /class/new/
	# Returns the class as JSON
	url(r'^class/new/$', renderView.ClassView, name='ClassView'),

	#ex: /class/5/
	# Returns the class as JSON
	url(r'^class/(?P<class_id>\d+)/$', renderView.ClassView, name='ClassView'),

	#ex: /interface/5/
	# Returns the class as JSON
	url(r'^interface/new/$', renderView.InterfaceView, name='InterfaceView'),

	#ex: /interface/5/
	# Returns the class as JSON
	url(r'^interface/(?P<interface_id>\d+)/$', renderView.InterfaceView, name='InterfaceView'),

	url(r'^class/(?P<class_id>\d+)/method/(?P<method_id>\d+)/$', renderView.MethodView, name='MethodView'),
	
	url(r'^class/(?P<class_id>\d+)/method/new/$', renderView.MethodView, name='MethodView'),

	url(r'^class/(?P<class_id>\d+)/member/(?P<member_id>\d+)/$', renderView.MemberView, name='MemberView'),
	
	url(r'^class/(?P<class_id>\d+)/member/new/$', renderView.MemberView, name='MemberView'),

	#ex: /package/5/
	# Returns the class as JSON
	url(r'^package/(?P<package_id>\d+)/$', renderView.ClassView, name='ClassView'),
	
	url(r'login/$', renderView.LoginView, name='LoginView'),

	url(r'logout/$', renderView.LogoutView, name='LogoutView'),
)
