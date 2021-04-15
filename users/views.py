import json
import re
#import bcrypt
#import jwt
#import string
#import random

from django.views         import View
from django.http          import JsonResponse
from django.db.models     import Q
#from django.core.mail     import EmailMessage

from users.models         import User, Address, Review, UserLike, Comment


class FindIdView(View):
    def post(self, request):
        data = json.loads(request.body)
        email_check = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        try:
            name  = data['name']
            email = data['email']

            if not email_check.match(email):
                return JsonResponse({'MESSAGE':'EMAIL_TYPE_ERROR'}, status=400)

            if not User.objects.filter(Q(name=name) & Q(email=email)).exists():
                return JsonResponse({'MESSAGE':'INVALID_EMAIL_OR_INVALID_NAME'}, status=400)

            user = User.objects.get(email=email)

            return JsonResponse({'MESSAGE':user.identification}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)






