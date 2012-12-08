from django.contrib import admin
from uml.models import Class
from uml.models import Modifier
from uml.models import Member
from uml.models import Parameter
from uml.models import Method
from uml.models import Interface
from uml.models import Variable
from uml.models import ReturnType
from uml.models import Package

admin.site.register(Class)
admin.site.register(Modifier)
admin.site.register(Member)
admin.site.register(Parameter)
admin.site.register(Method)
admin.site.register(Interface)
admin.site.register(Variable)
admin.site.register(ReturnType)
admin.site.register(Package)
