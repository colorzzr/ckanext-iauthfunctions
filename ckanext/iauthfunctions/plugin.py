import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import c, request
# from ckan.common import 

# def tag_show_test(context, data_dict=None):
# 	return {'success' : False}

def my_auth(context, data_dict=None):
	print("-------my_auth------")
	print(request.url)
	if c.user != 'hp':
		return {'success' : False}
	else:
		return {'success' : True}

	# return {'success' : False}


def my_auth_func(context, data_dict=None):
	# print("-------my_auth_func------")
	# if user are not logined it would directly fail
	toolkit.check_access('my_auth', context, None)
	


def site_read_test(context, data_dict=None):
	print('------site_read_test------')
	# print(context['user'])
	# note here if user are not login then the user attribute IS NOT in the CONTEXT!
	try:
		print("test!" + request.url)
		if context['user'] != 'hp':
			if request.url == 'http://localhost:5000/about':
				return {'success' : False}
			else:
				return {'success' : True}
		else:
			return {'success':True}

	except toolkit.NotAuthorized:
		# p.toolkit.abort will log user out when auth function fails, which may not be desired
		print("------test------")
		toolkit.abort(403, 'Not authorized to see this tab')

def group_create(context, data_dict=None):
	# Get the user name of the logged-in user.
	user_name = context['user']
	# print("------context------")
	# print(context)
	# print(context['model'])

	# Get a list of the members of the 'curators' group.]
	try:
		members = toolkit.get_action('member_list')(
		data_dict={'id': 'onlyicanadd', 'object_type': 'user'})
		# print(members)
	except toolkit.ObjectNotFound:
		# The curators group doesn't exist.
		return {'success': False,
		'msg': "The curators groups doesn't exist, so only sysadmins "
		"are authorized to create groups."}

	# 'members' is a list of (user_id, object_type, capacity) tuples, we're
	# only interested in the user_ids.
	member_ids = [member_tuple[0] for member_tuple in members]
	# print(member_ids)

	# We have the logged-in user's user name, get their user id.
	convert_user_name_or_id_to_id = toolkit.get_converter(
	'convert_user_name_or_id_to_id')
	user_id = convert_user_name_or_id_to_id(user_name, context)
	# print(user_id)

	# print(type(user_id), type(member_ids[0]))\
	
	# Finally, we can test whether the user is a member of the curators group.
	if user_id in member_ids:
		# print("in")
		return {'success': True}
	else:
		# print("not in")
		return {'success': False,
		'msg': 'Only curators are allowed to create groups'}

class IauthfunctionsPlugin(plugins.SingletonPlugin):
	plugins.implements(plugins.IAuthFunctions)
	plugins.implements(plugins.IActions)

	# IAuthFunctions
	def get_auth_functions(self):
		return {
			'group_create': group_create,
			# 'site_read':site_read_test,
			'my_auth': my_auth,
		}


	# IActions
	def get_actions(self):
		actions_dict = {
			'my_auth': my_auth_func
		}
		return actions_dict
