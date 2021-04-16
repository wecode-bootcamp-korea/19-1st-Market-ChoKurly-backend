import json
import bcrypt
import string
import random
import my_settings

from django.views         import View
from django.http          import JsonResponse
from django.db.models     import Q
from django.core.mail     import EmailMessage

from users.models         import User, Address, Review, UserLike, Comment

class FindIdView(View):
    def post(self, request):

        try:
            data  = json.loads(request.body)
            name  = data['name']
            email = data['email']

            if not my_settings.EMAIL_CHECK.match(email):
                return JsonResponse({'MESSAGE':'EMAIL_TYPE_ERROR'}, status=400)

            if not User.objects.filter(Q(name=name) & Q(email=email)).exists():
                return JsonResponse({'MESSAGE':'INVALID_EMAIL_OR_INVALID_NAME'}, status=400)

            user = User.objects.get(email=email)

            return JsonResponse({'MESSAGE':user.identification}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'MESSAGE':'JSON_Decode_Error'}, status=400)

class FindPwView(View):
    def post(self, request):
        data = json.loads(request.body)
        length = 8
        string_pool = string.ascii_letters + string.digits
        auth_num = ''

        for i in range(length):
            auth_num += random.choice(string_pool)

        try:
            name = data['name']
            identification = data['identification']
            email = data['email']

            if not User.objects.filter(Q(name=name) & Q(identification=identification) & Q(email=email)).exists():
                return JsonResponse({'MESSAGE':'INVALID_NAME OR IDENTIFICATION OR EMAIL'})

            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(auth_num.encode('utf-8'), salt)
            hashed_password = hashed_password.decode('utf-8')

            user = User.objects.get(email=email)
            user.password = hashed_password
            user.save()

            email = EmailMessage('[CHOKURLY] 이메일 인증번호', auth_num, to=[email])
            email.send()

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)










