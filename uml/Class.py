from array import *
from uml.models import *

def getClass(class_id):
	c = Class.objects.get(id=class_id)
	modifiers = Modifier.objects.filter(modifier_class=c)
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

	result['id'] = c.id
	result['class_name'] = c.class_name
	result['methods'] = getMethods(c)
	result['members'] = getMembers(c)
	#result['package'] = c.class_package
	result['extends'] = c.class_extends
	result['implements'] = c.class_implemets.all()
	return result;

def getClassJson(class_id):
	c = Class.objects.get(id=class_id)
	modifiers = Modifier.objects.filter(modifier_class=c)
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

	result['id'] = c.id
	result['class_name'] = c.class_name
	result['methods'] = getMethods(c)
	result['members'] = getMembers(c)
	#result['package'] = c.class_package
	if c.class_extends:
		result['extends'] = c.class_extends.id
	imps = c.class_implemets.all()
	#result['implements'] = list()
	#for imp in imps:
	#	result['implements'].append(imp.id)
	return result;

def getEmptyClass():
	result = {}
	result['modifiers'] = list()
	result['access'] = ''

	result['id'] = -1
	result['class_name'] = ""
	result['methods'] = list()
	result['members'] = list()
	#result['package'] = c.class_package
	result['implements'] = list()
	return result;


def getImplements(c):
	return Interface.objects.filter(id=Implements.objects.filter)

def getClassName(class_id):
	return 'Class'

def getMethods(c):
	ms = Method.objects.filter(method_class=c)
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

def getMembers(c):
	ms = Member.objects.filter(member_class=c)
	Members = []
	for member in ms:	
		Members.append(getMember(member))
	return Members

def getMember(member):
	m = {}
	m['name'] = member.member_variable.variable_name
	m['id'] = member.id
	if member.member_variable.variable_class == None:
		m['type'] = member.member_variable.variable_type
	else:
		m['type'] = member.member_variable.variable_class.class_name
	return m

def getPackage(class_id):
	return 'com.android'

	
