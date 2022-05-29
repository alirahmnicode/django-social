from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from djoser.views import UserViewSet
from .register_code import Code

class SignUpView(UserViewSet):
    def perform_create(self, serializer):
        code = Code(self.request, digit=6, save=True)
        code = code.generator()
        # send sms
        # give jwt
        return super().perform_create(serializer)

class ActivateAcoountView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, **kwrags):
        # get new code for activate account
        pass

    def post(self, request, **kwrags):
        # activate account
        user = request.user
        activate_code = request.session.get('code')
        user_code = request.data.get('code')
        if int(activate_code) == int(user_code):
            user.is_active_account = True
            user.save()
            return Response('account is activates.', status=status.HTTP_200_OK)
        else:
            return Response('code is wrange!', status=status.HTTP_400_BAD_REQUEST)