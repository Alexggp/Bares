from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseRedirect
from django.template import RequestContext, loader
from MisBares.models import Bar
from django.core import serializers

# Create your views here.


from django.views.decorators.csrf import csrf_exempt




def bares(request, resource):

    data = serializers.serialize("json", Bar.objects.all())

    
    template = loader.get_template('MisBares/base.html')
    context = RequestContext(request, {'bar_list':data})
    return HttpResponse(template.render(context))
    
  
@csrf_exempt   
def addBar(request):
    
    
    json=request.POST[u'priceForm']
    
    return HttpResponse(json)
