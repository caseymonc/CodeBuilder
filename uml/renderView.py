from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import os
from uml.models import Class, Interface, Package
from Class import *
from Interface import *
from Method import *
from Member import *
from Type import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User





def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/model/login/')
	classes = Class.objects.all()
	interfaces = Interface.objects.all()
	packages = Package.objects.all()
	return render_to_response('split.html', { 'classes': classes , 'interfaces' : interfaces, 'packages' : packages})

def ClassView(request, class_id = -1):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/model/login/')
	if class_id > 0:
		c = getClass(class_id)
	else:
		c = getEmptyClass()
	
	basic_types = getBasicTypes()
	data_types = getDataStructureTypes()
	class_types = getClassTypes()
	interfaces = Interface.objects.all()
	return render_to_response('class.html', { 'class' : c , 'basic_types' : basic_types, 'data_types' : data_types, 'class_types' : class_types, 'interfaces' : interfaces})

def InterfaceView(request, interface_id = -1):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/model/login/')
	if interface_id == -1:
		i = getEmptyInterface()
	else:
		i = getInterface(interface_id)
	interfaces = Interface.objects.all()
	return render_to_response('interface.html', { 'interface' : i , 'interfaces' : interfaces})

def MethodView(request, class_id, method_id = -1):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/model/login/')
	if method_id == -1:
		m = getEmptyMethod()
	else:
		m = getMethod(method_id)
	m['class_id'] = class_id
	basic_types = getBasicTypes()
	data_types = getDataStructureTypes()
	class_types = getClassTypes()
	return render_to_response('method.html', { 'method' : m, 'basic_types' : basic_types, 'data_types' : data_types, 'class_types' : class_types})

def MemberView(request, class_id, member_id = -1):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/model/login/')
	if member_id == -1:
		m = getEmptyMember()
	else:
		m = getMemberJSON(member_id)
	m['class_id'] = class_id
	basic_types = getBasicTypes()
	data_types = getDataStructureTypes()
	class_types = getClassTypes()
	return render_to_response('member.html', { 'member' : m, 'basic_types' : basic_types, 'data_types' : data_types, 'class_types' : class_types})

def LoginView(request):
	return render_to_response('login.html')

def Login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/model/')
        else:
            return HttpResponseRedirect('/model/login/')
    else:
        return HttpResponseRedirect('/model/login/')

def LogoutView(request):
	logout(request)
	return HttpResponseRedirect('/model/login/')

def Register(request):
	username = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	user = User.objects.create_user(username, email, password)
	user.save()
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/model/')
		else:
			return HttpResponseRedirect('/model/login/')
	else:
		return HttpResponseRedirect('/model/login/')

