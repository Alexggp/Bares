from django.http import HttpResponse
from django.template import RequestContext, loader
from MisBares.models import Bar
from django.core import serializers
# Create your views here.




def bares(request):


    #bar_list=Bar.objects.all()
    data = serializers.serialize("json", Bar.objects.all())

    
    template = loader.get_template('MisBares/base.html')
    context = RequestContext(request, {'bars':data})
    return HttpResponse(template.render(context))
    
