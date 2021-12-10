from django import template

register = template.Library()

def slice(value, arg):
	"""
	This function slices string object..
	"""
	if len(value) <= 50:
		return value
	return str(value[:arg] + "...")

register.filter('slice', slice)