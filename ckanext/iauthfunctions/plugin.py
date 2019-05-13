import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import c

# This the hooked autherization function
def my_auth(context, data_dict=None):
	if c.user != 'hp':
		return {'success' : False}
	else:
		return {'success' : True}


# This is the function that autherization hooked and will be called in the about function
def my_auth_func(context, data_dict=None):
	toolkit.check_access('my_auth', context, None)
	

class IauthfunctionsPlugin(plugins.SingletonPlugin):
	plugins.implements(plugins.IAuthFunctions)
	plugins.implements(plugins.IActions)

	# IAuthFunctions
	def get_auth_functions(self):
		return {
			'my_auth': my_auth,
		}

	# IActions
	def get_actions(self):
		actions_dict = {
			'my_auth': my_auth_func
		}
		return actions_dict
