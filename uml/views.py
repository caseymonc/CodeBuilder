from django.http import HttpResponse
import json
from Class import *
from models import *

# Create your views here.
def index(request):
	response_data = {}
	response_data['result'] = 'failed'
	response_data['message'] = 'You messed up'
	return HttpResponse(json.dumps(response_data), mimetype="application/json")

def RequestClass(request, class_id = -1):
	if request.method == 'GET':
		return HttpResponse(json.dumps(getClassJson(class_id)), mimetype="application/json")
	elif request.method == 'POST':
		values = request.POST.dict()
		response = {}
		if class_id != -1:
			response = updateClass(values, class_id)
		else:
			response = insertClass(values)
		
		return HttpResponse(json.dumps(response), mimetype="application/json")
	elif request.method == 'DELETE':
		if class_id == -1:
			return HttpResponse("Unsupported Method")	
		else:
			Class.objects.get(id=class_id).delete()
			return HttpResponse("OK")
	else:
		return HttpResponse("Unsupported Method")

def updateClass(json, class_id):
	c = Class.objects.get(id=class_id)
	saveClass(json, c)
	saveClassModifiers(json, c)
	return {'class_id' : c.id, 'class_name' : c.class_name}

def insertClass(json):
	c = Class()
	saveClass(json, c)
	saveClassModifiers(json, c)
	return {'class_id' : c.id, 'class_name' : c.class_name}

def saveClass(json, c):
	if 'class_name' in json:
		c.class_name = json['class_name']
	
	if 'class_extends' in json:
		if json['class_extends'].split(":")[0] == 'class':
			c.class_extends = Class.objects.get(id=json['class_extends'].split(":")[1])
	
	if 'interfaces' in json:
		interfaces = json['interfaces'].split(',')
		c.class_implemets.clear()	
		for interface_id in interfaces:
			c.class_implemets.add(Interface.objects.get(id=interface_id))
	c.save()

def saveClassModifiers(json, c):
	Modifier.objects.filter(modifier_class=c).delete()
	if json['access'] == 'PU':
		m = Modifier()
		m.modifier_class = c
		m.modifier_modifier = 'PU'
		m.save()
	
	if json['final'] == '1':
		m = Modifier()
		m.modifier_class = c
		m.modifier_modifier = 'FI'
		m.save()

	if json['abstract'] == '1':
		m = Modifier()
		m.modifier_class = c
		m.modifier_modifier = 'AB'
		m.save()		
	
		

def RequestMethods(request, class_id, method_id = -1):
	if request.method == 'GET':
		return HttpResponse(json.dumps(getMethods(class_id)), mimetype="application/json")
	elif request.method == 'POST':
		values = request.POST.dict()
		
		if method_id != -1:
			updateMethod(values, class_id, method_id)
		else:
			insertMethod(values, class_id)
		
		return HttpResponse("OK")
	elif request.method == 'DELETE':
		if class_id == -1 or method_id == -1:
			return HttpResponse("Unsupported Method")	
		else:
			Method.objects.get(id=method_id).delete()
			return HttpResponse("OK")
	else:
		return HttpResponse("Unsupported Method")

def updateMethod(json, class_id, method_id):
	m = Method.objects.get(id=method_id)
	if 'return' in json and json['return'] != 'void':
		m.method_returnType = getReturnType(json)
	saveMethod(json, m)
	saveMethodModifiers(json, m)

def insertMethod(json, class_id):
	c = Class.objects.get(id=class_id)	
	m = Method()
	m.method_class = c
	if 'return' in json and json['return'] != 'void':
		m.method_returnType = getReturnType(json)
	saveMethod(json, m)
	saveMethodModifiers(json, m)

def getReturnType(json):
	rt = ReturnType()
	
	if json['return'].split(":")[0] == 'class':
		rt.return_type_class = Class.objects.get(id=json['return'].split(":")[1])
	else:
		rt.return_type_type = json['return'].split(":")[1]
	rt.save()
	return rt

def saveMethod(json, m):
	if 'method_name' in json:
		m.method_name = json['method_name']
	m.save()

def saveMethodModifiers(json, method):
	Modifier.objects.filter(modifier_method=method).delete()
	if json['access'] != '':
		m = Modifier()
		m.modifier_method = method
		m.modifier_modifier = json['access']
		m.save()
	
	if json['final'] == '1':
		m = Modifier()
		m.modifier_method = method
		m.modifier_modifier = 'FI'
		m.save()

	if json['abstract'] == '1':
		m = Modifier()
		m.modifier_method = method
		m.modifier_modifier = 'AB'
		m.save()	

def RequestMembers(request, class_id, member_id = -1):
	if request.method == 'GET':
		return HttpResponse("Unsupported Method")
	elif request.method == 'POST':
		values = request.POST.dict()
		
		if member_id != -1:
			updateMember(values, class_id, member_id)
		else:
			insertMember(values, class_id)
		
		return HttpResponse("OK")
	elif request.method == 'DELETE':
		if class_id == -1 or member_id == -1:
			return HttpResponse("Unsupported Method")	
		else:
			Member.objects.get(id=member_id).delete()
			return HttpResponse("OK")
	else:
		return HttpResponse("Unsupported Method")

def updateMember(json, class_id, member_id):
	m = Member.objects.get(id=member_id)
	getVariable(m.member_variable, json, m)
	saveMember(json, m)
	saveMemberModifiers(json, m)

def insertMember(json, class_id):
	c = Class.objects.get(id=class_id)	
	m = Member()
	m.member_class = c
	m.member_variable = getVariable(Variable(), json, m)
	saveMember(json, m)
	saveMemberModifiers(json, m)

def getVariable(v, json, m):
	v.variable_name = json['member_name']
	if 'member_name' in json:
		v.variable_name = json['member_name']
	if 'member_type' in json:
		if json['member_type'].split(":")[0] == 'class':
			v.variable_class = Class.objects.get(id=json['return'].split(":")[1])
		else:
			v.variable_type = json['member_type'].split(":")[1]
	v.save()
	return v

def saveMemberModifiers(json, member):
	Modifier.objects.filter(modifier_member=member).delete()
	if json['access'] != '':
		m = Modifier()
		m.modifier_member = member
		m.modifier_modifier = json['access']
		m.save()
	
	if json['final'] == '1':
		m = Modifier()
		m.modifier_member = member
		m.modifier_modifier = 'FI'
		m.save()

	if json['abstract'] == '1':
		m = Modifier()
		m.modifier_member = member
		m.modifier_modifier = 'AB'
		m.save()

def saveMember(json, m):
	
	m.save()

def RequestInterface(request, interface_id = -1):
	if request.method == 'GET':
		return HttpResponse("Unsupported Method")
	elif request.method == 'POST':
		values = request.POST.dict()
		response = {}
		if interface_id != -1:
			response = updateInterface(values, interface_id)
		else:
			response = insertInterface(values)
		
		return HttpResponse(json.dumps(response), mimetype="application/json")
	elif request.method == 'DELETE':
		if interface_id == -1:
			return HttpResponse("Unsupported Method")	
		else:
			Interface.objects.get(id=interface_id).delete()
			return HttpResponse("OK")
	else:
		return HttpResponse("Unsupported Method")

def updateInterface(json, interface_id):
	c = Interface.objects.get(id=interface_id)
	saveInterface(json, c)
	return {'interface_id' : c.id, 'interface_name' : c.interface_name, 'interface_extends' : c.interface_extends.id}

def insertInterface(json):
	c = Interface()
	saveInterface(json, c)
	return {'interface_id' : c.id, 'interface_name' : c.interface_name, 'interface_extends' : c.interface_extends.id}

def saveInterface(json, c):
	if 'interface_name' in json:
		c.interface_name = json['interface_name']
	
	if 'interface_extends' in json:
		c.interface_extends = Interface.objects.get(id=json['interface_extends'])
	c.save()

def RequestIMethods(request, interface_id):
	return HttpResponse("You're looking at methods for interface %s." % interface_id)

def RequestIMethod(request, interface_id, method_id):
	return HttpResponse("You're looking at method %s for interface." % method_id)

