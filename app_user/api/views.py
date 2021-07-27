from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

from rest_framework.response import Response

from django.contrib.auth.models import User, Group


class RegisterAPI(APIView):
	
	def post(self, request, format=None):

		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		
		
		try:


			if password1==password2:
				if username == '' or email == '' or password1 =='':
					response = {
						'message' : 'Data tidak valid' 
					}			
					status = '404'



				else:





					user = User()
					try:
						user.username = username
						user.save()
					except:
						response = {
							'message' : 'Username telah terdaftar' 
						}			
						status = '404'
						responses={
							'response'	: response,
							'status'	: status,
						}
						return Response(responses, status)
					user.first_name = first_name
					user.last_name = last_name
					user.email = email
					user.password = make_password(password1)
					user.is_active = True # Deactivate account till it is confirmed
					user.save()
					
					my_group = Group.objects.get(name='user_access')
					my_group.user_set.add(user) 

					# current_site = get_current_site(request)
					# subject = 'Activate Your MySite Account'
					# message = render_to_string('registration/account_activation_email.html', {
					# 	'user': user,
					# 	'domain': current_site.domain,
					# 	'uid': user,
					# 	'token': get_otp_code(user.pk),
					# })
					# user.email_user(subject, message)
					response = {
							'message' : 'Sukses register' 
						}
					status = '201'

			else:
				response = {
						'message' : 'password tidak valid' 
					}			
				status = '404'

			# response = 'sukses'
			# status = '201'	
		except Exception as e:
			print(e)
			response = {
				'message' : 'gagal, '+ str(e) 
			}			
			status = '404'

		responses={
			'response'	: response,
			'status'	: status,
		}
		return Response(responses, status)	