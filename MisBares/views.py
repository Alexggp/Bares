from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseRedirect
from django.template import RequestContext, loader
from MisBares.models import Bar_db
from django.core import serializers
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt # to avoid  403 FORBIDDEN error

login_form=AuthenticationForm()


def logout_user(request):
  logout(request)

  return HttpResponseRedirect('/')


def bares(request, resource):
    user_name=request.user.username

    template = loader.get_template('MisBares/base.html')
    context = RequestContext(request, {'user_name':user_name ,'login_form':login_form})
    return HttpResponse(template.render(context))
    


def initialize(request):

    EastGet=request.GET[u'East']
    WestGet=request.GET[u'West']
    NorthGet=request.GET[u'North']
    SouthGet=request.GET[u'South']
    
    bar_list = Bar_db.objects.filter(Q(latitude__lte = NorthGet), 
                                    Q(latitude__gte = SouthGet),
                                    Q(longitude__lte = EastGet),
                                    Q(longitude__gte = WestGet) )
    
    data = serializers.serialize("json", bar_list)   
    


    return HttpResponse(data)


  
@csrf_exempt   
def addBar(request):

    namePost=request.POST[u'nameForm']
    streetPost=request.POST[u'streetForm']
    pricePost=request.POST[u'priceForm']
    litrePost=request.POST[u'litreForm']
    tapaPost=request.POST[u'tapaForm']
    latPost=request.POST[u'latForm']
    lonPost=request.POST[u'lonForm']
    
    if (tapaPost=="false"):
        tapaPost=False
    
    if (Bar_db.objects.filter(Q(name=namePost),Q(street=streetPost)).exists()):  
                                                                    #checks if the bar already exists, sends error message if true
        data='error'
    else:
        r=Bar_db(name=namePost,street=streetPost,price=pricePost,litre=litrePost,tapa=tapaPost,latitude=latPost,longitude=lonPost)
        r.save()
        data = serializers.serialize("json", Bar_db.objects.all())

    return HttpResponse(data)
