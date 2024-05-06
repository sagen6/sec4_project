from django.shortcuts import render, HttpResponse
from Home.models import *

# Create your views here.
def index(Request):
    return render(Request,'kmc.html')
    #return HttpResponse("This is my homepage")
def contact(Request):
    return render(Request ,'contact.html')
def photos(Request):
    return render(Request ,'photos.html')

def teachers(request):
    if(request.method=="POST"):
        data=request.POST
        result=teacher.objects.filter(name=data.get("name")) 
        name=result[0].name
        mobile=result[0].mobile
        email=result[0].email
        # name=data.get("teacher")
        # mobile=data.get("mobile")
        # email=data.get("email")
        context={"name":name,"mobile":mobile,"email":email}
        # context={"teacher":name}
        return render(request,"search_results.html",context)
    return render(request,"teacher.html")