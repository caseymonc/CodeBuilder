from array import *
from uml.models import *

def getMemberJSON(member_id):
	m = Member.objects.get(id=member_id)
	modifiers = Modifier.objects.filter(modifier_member=m)
	variable = m.member_variable
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
	result['variable'] = variable
	return result;

def getEmptyMember():
	result = {}
	result['modifiers'] = list()
	result['access'] = ''

	result['id'] = -1
	result['variable'] = {}
	result['variable']['variable_class'] = None
	result['variable']['variable_name'] = ''
	result['variable']['variable_type'] = ''
	result['variable']['variable_isArray'] = False
	
	return result;
