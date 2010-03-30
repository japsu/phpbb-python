# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def protected_resource(request):
    return render_to_response("protected.html", context_instance=RequestContext(request, {}))

