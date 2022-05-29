from django.shortcuts import render
from djoser.views import UserViewSet
from .register_code import Code

class SignUpView(UserViewSet):
    def perform_create(self, serializer):
        code = Code(self.request, digit=6, save=True)
        code = code.generator()
        # send sms
        # give jwt
        return super().perform_create(serializer)