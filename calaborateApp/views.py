from django.template import RequestContext, Template, Context

# Create your views here.
@csrf_exempt 
def index(request):
	 return render_to_response('index.html', {}, context_instance=RequestContext(request))