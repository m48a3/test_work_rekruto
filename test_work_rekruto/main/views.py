from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):

    return HttpResponseRedirect('/hello/?name=Rekruto&message=Давай дружить!')

def hello(request):
    name = request.GET.get("name", "Кто-нибудь")
    message = request.GET.get("message","Давайте дружить!")
    output = "<p>Hello {0}! {1}!</p>".format(name,message)
    return HttpResponse(output)
