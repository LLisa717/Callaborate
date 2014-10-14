from django.template import RequestContext, Template, Context
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render_to_response
# Create your views here.
@csrf_exempt 
def index(request):
	 return render_to_response('index.html', {}, context_instance=RequestContext(request))