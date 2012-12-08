from array import *
from uml.models import *

def getInterface(interface_id):
	i = Interface.objects.get(id=interface_id)
	modifiers = Modifier.objects.filter(modifier_interface=i)
	result = {}
	result['modifiers'] = list()
	for modifier in modifiers:
		result['modifiers'].append(modifier.modifier_modifier)
	if 'PU' in result['modifiers']:
		result['access'] = 'public'
	elif 'PR' in result['modifiers']:
		result['access'] = 'private'
	elif 'PO' in result['modifiers']:
		result['access'] = 'protected'
	else:
		result['access'] = ''
	result['id'] = i.id
	result['name'] = i.interface_name
	result['methods'] = getMethods(i)
	result['interface_extends'] = i.interface_extends
	return result;

def getEmptyInterface():
	result = {}
	result['id'] = -1	
	result['modifiers'] = list()
	result['access'] = ''

	result['name'] = ''
	result['methods'] = list()
	return result;

def getMethods(i):
	ms = Method.objects.filter(method_interface=i)
	Methods = list()
	for method in ms:
		Methods.append(getMethod(method))
	return Methods

def getMethod(method):
	modifiers = Modifier.objects.filter(modifier_method=method)
	m = {}
	m['name'] = method.method_name
	m['id'] = method.id
	
	if method.method_returnType == None:
		m['type'] = 'void'
	elif method.method_returnType.return_type_class == None:
		m['type'] = method.method_returnType.return_type_type
	else:
		m['type'] = method.method_returnType.return_type_class.class_name

	m['modifiers'] = list()
	for modifier in modifiers:
		m['modifiers'].append(modifier.modifier_modifier)

	if 'PU' in m['modifiers']:
		m['access'] = 'public'
	elif 'PR' in m['modifiers']:
		m['access'] = 'private'
	elif 'PO' in m['modifiers']:
		m['access'] = 'protected'
	else:
		m['access'] = ''

	return m

		
