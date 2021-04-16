import json
import bcrypt
import jwt
import my_settings

from django.db          import transaction
from django.http        import JsonResponse
from django.views       import View

from .models            import User, Address

class UserView(View):
    def post(self, request):
        try:
            data                 = json.loads(request.body)
            LENGTH               = 0
            identification       = data['id']
            password             = data['password']
            name                 = data['name']
            email                = data['email']
            phone_number         = data['phone_number']
            birth_date           = data['birthdate']
            gender               = data['gender']
            address              = data['address']

            if len(name) <= LENGTH:
                return JsonResponse({'MESSAGE':'NAME_ERRROR'}, status=400)

            if len(birth_date) <= LENGTH:
                return JsonResponse({'MESSAGE':'BIRTHDATE_ERRROR'}, status=400)

            if len(gender) <= LENGTH:
                return JsonResponse({'MESSAGE':'GENDER_ERRROR'}, status=400)

            if len(address) <= LENGTH:
               return JsonResponse({'MESSAGE':'ADDRESS_INPUT_ERROR'}, status=400)

            if not my_settings.identification_check.match(identification):
                return JsonResponse({'MESSAGE':'INVALID_ID_ERROR'}, status=400)

            if not my_settings.password_check.match(password):
                return JsonResponse({'MESSAGE':'INVALID_PW_ERROR'}, status=400)
                
            if not my_settings.email_check.match(email):
                return JsonResponse({'MESSAGE':'INVALID_EMAIL_ERROR'}, status=400)
            
            if not my_settings.phone_check.match(phone_number):
                return JsonResponse({'MESSAGE':'INVALID_PHONENUMBER'}, status=400)

            if User.objects.filter(identification = identification).exists():
                return JsonResponse({'MESSAGE':'ID_DUPLICATE_ERROR'}, status=400)
                
            if User.objects.filter(phone_number = phone_number).exists():
                return JsonResponse({'MESSSAGE':'PHONE_NUMBER_DUPLICATE_ERROR'}, status=400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'MESSSAGE':'EMAIL_DUPLICATE_ERROR'}, status=401)

            with transaction.atomic():
                hashed_pw = bcrypt.hashpw( password.encode('utf-8'),  bcrypt.gensalt() )    
                user = User.objects.create(
                            identification = identification ,
                            password       = hashed_pw.decode('utf-8') ,
                            name           = name ,
                            email          = email ,
                            phone_number   = phone_number ,
                            birthdate      = birth_date ,
                            gender         = gender )

                user_address = Address.objects.create(
                            address     = address,
                            user        = user,
                            is_default  = data['is_defalut'])

                user_address.save()

                return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)



