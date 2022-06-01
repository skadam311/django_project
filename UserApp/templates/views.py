from asyncio import events
from django.shortcuts import render,redirect
from django.http import HttpResponse
from UserApp.models import UserInfo
import folium
import geocoder
from AdminApp.models import Category,EventList

# Create your views here.

def Home(request):
    cats=Category.objects.all()
    events=EventList.objects.all()
    return render(request,'index.html',{"cats":cats,"events":events})
def Address(request):
   m=folium.Map(location=[],zoom_start=2)
   folium.Marker([].add_to(m))
   m=m._repr_html_()
   context={
       'm': m,
   }
   return render(request,'Address.html',context)
def Login(request):
    cats = Category.objects.all()
    if(request.method=="GET"):
        return render(request,"Login.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        pwd =request.POST["pwd"]
        try:
            u1 = UserInfo.objects.get(username = uname,password=pwd)            
        except:
            pass
        else:
            request.session["uname"] = uname
            u1.status='active'
            u1.save()
        return redirect(Home)
def SignUp(request):
    cats = Category.objects.all()
    if(request.method=="GET"):
        return render(request,"SignUp.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        pwd =request.POST["pwd"]
        #Check if user already present
        try:
            u1 = UserInfo.objects.get(username = uname)
        except:
            #User Doesnt exist
            u1 = UserInfo(uname,pwd,'inactive')
            u1.save()
            return redirect(Home)
        else:
            return HttpResponse("User already exists..")

