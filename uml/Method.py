from array import *
from uml.models import *

def getMethod(method_id):
	m = Method.objects.get(id=method_id)
	modifiers = Modifier.objects.filter(modifier_method=m)
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

	result['id'] = m.id
	result['method_name'] = m.method_name
	return result;

def getEmptyMethod():
	result = {}
	result['modifiers'] = list()
	result['access'] = ''

	result['id'] = -1
	result['method_name'] = ""
	return result;

