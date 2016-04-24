from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class home(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(home, self).dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        print request.GET
        return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        print request.POST
        return HttpResponse('Hello, World!')
