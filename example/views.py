from django.shortcuts import render
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import SlidingToken
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
class toks(APIView):
    def post(self,request):
        token=request.META.get("HTTP_AUTHORIZATION",'').split()[1]
        tokens=SlidingToken(token)
        tokens.blacklist()
        return HttpResponse('the token is blackListed')
class toks1(APIView):
    def post(self,request):
        token=request.META.get("HTTP_AUTHORIZATION",'').split()[1]
        try:
            tokens=SlidingToken(token)
            tokens.check_blacklist()
            return HttpResponse('the token is blackListed')
        except TokenError:
            return HttpResponse('the token is already blacklisted')

