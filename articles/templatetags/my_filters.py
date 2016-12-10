from django.template.defaultfilters import register
from django import template


register = template.Library() 


@register.filter(name='sort')
def sort(index,team):
	
	print team
	return index

@register.filter(name='has_group') 
def has_group(user, group_name):
	group_name = group_name.title()
	print group_name
	print user
	

	print "successful"
	return "successful"

