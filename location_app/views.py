from django.http import HttpResponseForbidden,HttpResponse
from django.shortcuts import render
from hashlib import sha256

# Create your views here.
api_key="rajasthan_hacks"
api_key=api_key.encode("utf-8")
api_key=sha256(api_key).hexdigest()[10:20]
#this value currently equals=8d777d5c27

def index(request,key):
    if key==api_key:
        return render(request,'location_app/loc.html')

    return HttpResponseForbidden("You are not authorized to access this software")





def position(request):
    if request.method == "POST":
        pass
    else:
        return HttpResponse("get request is not accepted")