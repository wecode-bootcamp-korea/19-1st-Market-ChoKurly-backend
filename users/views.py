import json
import my_settings

from django.views         import View
from django.http          import JsonResponse
from django.db.models     import Q

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










