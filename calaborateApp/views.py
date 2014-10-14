from django.shortcuts import render

# Create your views here.
@csrf_exempt 
def index(request):
	 return render_to_response('index.html', {}, context_instance=RequestContext(request))