# from app.api.v1.models.user_model import UserModel


# def token_required(func):
# 	'''checks validity of tokens'''
# 	@wraps(func)
#     def decorated(*args, **kwargs):
#     	"""Decorated function"""
#     	access_token = None
#         try:
#             authorization_header = request.headers.get('Authorization')
#             if authorization_header:
#                 access_token = authorization_header.split(' ')[1]
#             if access_token:
#                 user_id = UserModel.decode_token(access_token)['id']
#                 return func(user_id=user_id, *args, **kwargs)
#             return {'message':"Please login first, your session might have expired"}, 401
#         except Exception as e:
#             return {'message': 'An error occured while decoding token.', 'error':str(e)},400
#     return decorated

def check_for_blanks(variable_object):
    if variable_object.strip() == '':
        return 'All fields are required'
    return None
