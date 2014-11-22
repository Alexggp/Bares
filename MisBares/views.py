from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseRedirect
from django.template import RequestContext, loader
from MisBares.models import Bar_db
from django.core import serializers

# Create your views here.


from django.views.decorators.csrf import csrf_exempt # to avoid  403 FORBIDDEN error




def bares(request, resource):

    data = serializers.serialize("json", Bar_db.objects.all())    #debo restringir por coordenadas, primero localizacion js, luego query
  
    template = loader.get_template('MisBares/base.html')
    context = RequestContext(request, {'bar_list':data})
    return HttpResponse(template.render(context))
    
  
@csrf_exempt   
def addBar(request):

    namePost=request.POST[u'nameForm']
    streetPost=request.POST[u'streetForm']
    pricePost=request.POST[u'priceForm']
    litrePost=request.POST[u'litreForm']
    tapaPost=request.POST[u'tapaForm']
    latPost=request.POST[u'latForm']
    lonPost=request.POST[u'lonForm']
    
    
    if (Bar_db.objects.filter(name=namePost,street=streetPost).exists()):  #checks if the bar already exists, sends error message if true
        data='error'
    else:
        r=Bar_db(name=namePost,street=streetPost,price=pricePost,litre=litrePost,tapa=tapaPost,latitude=latPost,longitude=lonPost)
        r.save()
        data = serializers.serialize("json", Bar_db.objects.all())

    return HttpResponse(data)
