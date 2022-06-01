from asyncio import events
from django.shortcuts import render,redirect
from django.http import HttpResponse
from requests import session
from UserApp.models import UserDetails,BookEvent
import folium
import geocoder
from AdminApp.models import Category,EventList

# Create your views here.

def Home(request):
    cats=Category.objects.all()
    events=EventList.objects.all()
    return render(request,'index.html',{"cats":cats,"events":events})
def ShowEvent(request,eid):
    cats=Category.objects.all()
    cat=Category.objects.get(id=eid)
    events=EventList.objects.filter(category=eid)
    return render(request,'index.html',{"cats":cats,"events":events,"event_type":cat.event_type})
def ShowDetails(request,id):
    if(request.method=="GET"):
        cats=Category.objects.all()  
        event=EventList.objects.get(id=id)
        return render(request,'ShowEventDetails.html',{"cats":cats,"event":event})
    else:
        if("uname" in request.session):
            eid=request.POST["event_id"]
            person=request.POST["person"]
            user=UserDetails.objects.get(username=request.session["uname"])
            event=EventList.objects.get(id=eid)
            try:
                book=BookEvent.objects.get(user=user,event=event)
            except:
                book=BookEvent()
                book.user=user
                book.event=event
                book.person=person
                book.save()
                return redirect(Home)
            else:
                return HttpResponse("already booked ticket")
                
        else:  
            
            return redirect(Login) 
def ShowAllBookedTicket(request):
    cats=Category.objects.all()
    user=UserDetails.objects.get(username=request.session["uname"])
    booked_tickets=BookEvent.objects.filter(user=user)
    total=0
    for tkt in booked_tickets:
        total +=tkt.event.ticekt_amount * tkt.person
    request.session["total"]=total
         
    return render(request,"ShowAllBookedTicket.html",{"cats":cats,"booked_tickets":booked_tickets})
def Address(request):
    m=folium.Map(location=[18.516726,73.856255],zoom_start=2)
    folium.Marker([18.5203, 73.8567 ],tooltip="click for more",popup='Bal Gandnarava mandal').add_to(m)
    folium.Marker([18.515604, 73.781905 ],tooltip="click for more",popup='cafe co2 Resto and launch').add_to(m)
    folium.Marker([18.501284, 73.750161 ],tooltip="click for more",popup='cafe H2o Resto and launch').add_to(m)
    folium.Marker([18.516726, 73.856255 ],tooltip="click for more",popup='singhgad coolage vadgaon,pune').add_to(m)
    folium.Marker([18.59433, 73.709599],tooltip="click for more",popup='Hinjewadi flyawer,wakad').add_to(m)
 
    m=m._repr_html_()
    context={
        'm':m,
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
            u1 =   UserDetails.objects.get(username = uname,password=pwd)            
        except:
            pass
        else:
            request.session["uname"] = uname
            u1.status='active'
            u1.save()
        return redirect(Home)
def Logout(request):
    u1= UserDetails.objects.get(username=request.session["uname"])
    u1.status='inactive'
    u1.save()
    request.session.clear()
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
            u1 = UserDetails.objects.get(username= uname)
        except:
            #User Doesnt exist
            u1 =   UserDetails(uname,pwd,'inactive')
            u1.save()
            return redirect(Home)
        else:
            return HttpResponse("User already exists..")


