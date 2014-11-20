from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseRedirect
from django.template import RequestContext, loader
from MisBares.models import Bar
from django.core import serializers

# Create your views here.


from django.views.decorators.csrf import csrf_exempt # to avoid  403 FORBIDDEN error




def bares(request, resource):

    data = serializers.serialize("json", Bar.objects.all())

    
    template = loader.get_template('MisBares/base.html')
    context = RequestContext(request, {'bar_list':data})
    return HttpResponse(template.render(context))
    
  
@csrf_exempt   
def addBar(request):

    namePost=request.POST[u'nameForm']
    pricePost=request.POST[u'priceForm']
    latPost=request.POST[u'latForm']
    lonPost=request.POST[u'lonForm']
    
    
    if (Bar.objects.filter(latitude=latPost,longitude=lonPost).exists()):  #checks if the bar already exists, sends error message if true
        data='error'
    else:
        r=Bar(name=namePost,price=pricePost,latitude=latPost,longitude=lonPost)
        r.save()
        data = serializers.serialize("json", Bar.objects.all())

    return HttpResponse(data)
