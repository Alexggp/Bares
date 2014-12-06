from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseRedirect
from django.template import RequestContext, loader
from MisBares.models import Bar_db,BarImages_db,Rates_db
from MisBares.forms import UploadFileForm
from django.core import serializers
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt # to avoid  403 FORBIDDEN error
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile


login_form=AuthenticationForm()
file_form=UploadFileForm()

def logout_user(request):
  logout(request)

  return HttpResponseRedirect('/')


def bares(request):
    user_name=request.user.username

    template = loader.get_template('MisBares/base.html')
    context = RequestContext(request, {'user_name':user_name ,'login_form':login_form,'file_form':file_form})
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


@login_required  
@csrf_exempt   
def addBar(request):

    namePost=request.POST[u'nameForm']
    streetPost=request.POST[u'streetForm']
    pricePost=request.POST[u'priceForm']
    litrePost=request.POST[u'litreForm']
    tapaPost=request.POST[u'tapaForm']
    latPost=request.POST[u'latForm']
    lonPost=request.POST[u'lonForm']
    imgPost=request.FILES['imgForm']
    
    if (tapaPost=="false"):
        tapaPost=False
    
    if (Bar_db.objects.filter(Q(name=namePost),Q(street=streetPost)).exists()):  
                                                                    #checks if the bar already exists, sends error message if true
        data='error'
    else:
        r=Bar_db(name=namePost,street=streetPost,price=pricePost,litre=litrePost,tapa=tapaPost,latitude=latPost,longitude=lonPost)
        r.save()
        
        instance = BarImages_db(image=request.FILES['image'],name='nameiin')            
        instance.save()
        
        
        data = serializers.serialize("json", Bar_db.objects.all())

    return HttpResponse(data)



@csrf_exempt  
def images(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            barq = Bar_db.objects.get(pk=request.POST['bar_id'])
            instance = BarImages_db(bar=barq,image=request.FILES['image'])
            instance.save()
        
            
            return HttpResponse(request.POST['bar_id'])   
        else:
            return HttpResponseBadRequest('Form is not valid')
    
    elif request.method == 'GET':
        barq = Bar_db.objects.get(pk=request.GET[u'bar_id'])
        images_list= BarImages_db.objects.filter(bar=barq)
        data = serializers.serialize("json", images_list)
        return HttpResponse(data)
    else:
        return HttpResponseBadRequest('Method error')
        
@csrf_exempt  
def rates(request):

    if request.method == 'POST':
        points= request.POST[u'value']
        print points
        if 0 < int(points) < 10 :
            barq = Bar_db.objects.get(pk=request.POST[u'bar_id'])
            instance = Rates_db(bar=barq,points=points)
            instance.save()
            
            return HttpResponse(request.POST[u'bar_id'])   
        else:
            return HttpResponseBadRequest('Not valid range')
    
    elif request.method == 'GET':
        barq = Bar_db.objects.get(pk=request.GET[u'bar_id'])
        rates_list= Rates_db.objects.filter(bar=barq)
        data = serializers.serialize("json", rates_list)
        return HttpResponse(data)
    else:
        return HttpResponseBadRequest('Method error')
        

