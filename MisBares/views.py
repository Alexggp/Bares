from django.http import HttpResponse
from django.template import RequestContext, loader


# Create your views here.
def bares(request):
    template = loader.get_template('MisBares/base.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
