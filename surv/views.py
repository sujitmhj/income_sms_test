from django.shortcuts import render, HttpResponse
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class home(View):

    def get(self, request, *args, **kwargs):
    	print request.GET
        return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        print request.POST
        return HttpResponse('Hello, World!')
