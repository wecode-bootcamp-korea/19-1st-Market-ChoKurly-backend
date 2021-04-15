import json, re, bcrypt, jwt
from .models            import User, Address
from django.db.models   import Q
from django.http        import JsonResponse
from django.views       import View

class UserView(View):
    def post(self, request):

        try:
            data                 = json.loads(request.body)
            identification       = data['id']
            password             = data['password']
            name                 = data['name']
            email                = data['email']
            phone_number         = data['phone_number']
            birth_date           = data['birthdate']
            gender               = data['gender']
            address              = data['address']
            phone_check          = re.compile('^[0-9]{3}[0-9]{3,4}[0-9]{4}')
            identification_check = re.compile('^[0-9a-zA-Z]{6,16}$')
            password_check       = re.compile('^(?=.*[a-zA-Z0-9])(?=.*[a-zA-Z!@#$%^&*])(?=.*[0-9!@#$%^&*]).{10,16}$')
            email_check          = re.compile('^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$')


            if len(name) <= 0:

                return JsonResponse({'MESSAGE':'NAME_ERRROR'}, status=400)

            if len(birth_date) <= 0:

                return JsonResponse({'MESSAGE':'BIRTHDATE_ERRROR'}, status=400)

            if len(gender) <= 0:

                return JsonResponse({'MESSAGE':'GENDER_ERRROR'}, status=400)

            if len(address) <= 0:

                return JsonResponse({'MESSAGE':'ADDRESS_INPUT_ERROR'}, status=400)

            if not identification_check.match(identification):

                return JsonResponse({'MESSAGE':'INVALID_ID_ERROR'}, status=400)

            if not password_check.match(password):

                return JsonResponse({'MESSAGE':'INVALID_PW_ERROR'}, status=400)
                
            if not email_check.match(email):

                return JsonResponse({'MESSAGE':'INVALID_EMAIL_ERROR'}, status=400)
            
            if not phone_check.match(phone_number):

                return JsonResponse({'MESSAGE':'INVALID_PHONENUMBER'}, status=400)

            if User.objects.filter(identification = identification).exists():

                return JsonResponse({'MESSAGE':'ID_DUPLICATE_ERROR'}, status=400)
                
            if User.objects.filter(phone_number = phone_number).exists():

                return JsonResponse({'MESSSAGE':'PHONE_NUMBER_DUPLICATE_ERROR'}, status=400)

            if User.objects.filter(email = email).exists():

                return JsonResponse({'MESSSAGE':'EMAIL_DUPLICATE_ERROR'}, status=401)

            
            if bcrypt.hashpw( password.encode('utf-8'),  bcrypt.gensalt() ):
                hashed_pw = bcrypt.hashpw( password.encode('utf-8'),  bcrypt.gensalt() )
                
                User.objects.create(
                            identification = identification ,
                            password       = hashed_pw.decode('utf-8') ,
                            name           = name ,
                            email          = email ,
                            phone_number   = phone_number ,
                            birthdate      = birth_date ,
                            gender         = gender )

                
                user = User.objects.get(identification = identification)

                Address.objects.create(
                            address     = address,
                            user        = user,
                            is_default  = 1)

                return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

            
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)