from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext, loader
from MisBares.models import Bar_db,BarImages_db,Rates_db,Comments_db
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

  return HttpResponseRedirect('/bares')


def bares(request):
    user_name=request.user.username
    
    template = loader.get_template('MisBares/base.html')
    context = RequestContext(request, {'user_name':user_name ,'login_form':login_form,'file_form':file_form})
    request.session.set_test_cookie()
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
    
    if request.session.test_cookie_worked():
        print ">>>> TEST COOKIE WORKED!"
        request.session.delete_test_cookie()

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
      
        
        data = serializers.serialize("json", [r])

    return HttpResponse(data)

@csrf_exempt
def changeBar(request):

    bar_idPost=request.POST[u'bar_id']
    pricePost=request.POST[u'priceForm']
    litrePost=request.POST[u'litreForm']
    tapaPost=request.POST[u'tapaForm']

    
    if (tapaPost=="false"):
        tapaPost=False


    barq = Bar_db.objects.get(pk=bar_idPost)
    if (barq):
        barq.price=pricePost
        barq.litre=litrePost
        barq.tapa=tapaPost
        barq.save()
        data = serializers.serialize("json",[barq])
        return HttpResponse(data)

    else:
        return HttpResponseNotFound('No bar matches the id')



@csrf_exempt  
def images(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            barq = Bar_db.objects.get(pk=request.POST['bar_id'])
            instance = BarImages_db(bar=barq,image=request.FILES['image'])
            instance.save()
            data = serializers.serialize("json", [barq])
            
            return HttpResponse(data)   
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
        if 0 < int(points) <= 10 :
            if request.COOKIES.has_key( request.POST[u'bar_id'] ):
                instance = Rates_db.objects.get(pk=request.COOKIES[ request.POST[u'bar_id'] ])
                instance.points=points
                instance.save()
                
            else:      
                barq = Bar_db.objects.get(pk=request.POST[u'bar_id'])
                instance = Rates_db(bar=barq,points=points)
                instance.save()
          
            key=request.POST[u'bar_id']
            value=instance.pk
            max_age= 100 *24 * 60 * 60
            
            response = HttpResponse(request.POST[u'bar_id'])        
            response.set_cookie(key, value, max_age)

            return response
              
        else:
            return HttpResponseBadRequest('Not valid range')
    
    elif request.method == 'GET':
        barq = Bar_db.objects.get(pk=request.GET[u'bar_id'])
        rates_list= Rates_db.objects.filter(bar=barq)
        data = serializers.serialize("json", rates_list)
        return HttpResponse(data)
    else:
        return HttpResponseBadRequest('Method error')

      
@csrf_exempt  
def comments(request):

    if request.method == 'POST':
        if request.user.is_authenticated():            
            textPost=request.POST[u'text']
            bar_idPost=request.POST[u'bar_id']
            barq = Bar_db.objects.get(pk=bar_idPost)
            instance = Comments_db(bar=barq,author=request.user,author_name=request.user.username,text=textPost)
            instance.save()            
            return HttpResponse(bar_idPost)
        else:
            return HttpResponseForbidden('Authentication error')
        
        
    elif request.method == 'GET':
        barq = Bar_db.objects.get(pk=request.GET[u'bar_id'])
        if request.GET[u'first']=="true": 
            comment= Comments_db.objects.filter(bar=barq).order_by('-date')[:2]
            data = serializers.serialize("json", comment)
            return HttpResponse(data)
        else: 
            comment= Comments_db.objects.filter(bar=barq).order_by('-date')
            data = serializers.serialize("json", comment)
            return HttpResponse(data)
    else:
        return HttpResponseBadRequest('Method error')

def deleteComments(request):
    if request.method == 'GET':
        Comments_db.objects.get(pk=request.GET[u'cmnt_id']).delete()
        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest('Method error') 
