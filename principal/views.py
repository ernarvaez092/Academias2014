#encoding:utf-8
from principal.models import Monumento
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def index(request):    
    return render_to_response('index.html')

def services(request):    
    return render_to_response('services.html')

def staff(request):
    monumentos = Monumento.objects.all()
    return render_to_response('staff.html',{'lista':monumentos},context_instance=RequestContext(request))    

def consultations(request):
    return render_to_response('consultations.html')

def prices(request):
    return render_to_response('prices.html')

def contacts(request):
    return render_to_response('contacts.html')

def historia(request, id):
    monumentos = get_object_or_404(Monumento, pk=id)    
    return render_to_response('historia.html',{'lista':monumentos},context_instance=RequestContext(request))

def WsJson(request):
    monumentos = serializers.serialize('json', Monumento.objects.all())
    return HttpResponse(monumentos, mimetype='application/json')



