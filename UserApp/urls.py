
from django.urls import path
from UserApp import views as UserApp_views
from UserApp import views

urlpatterns = [
    #path('',UserApp_views.indexs,name='indexs'),
    path('',views.Home),
    path('ShowEvent/<eid>',views.ShowEvent),
    path('ShowDetails/<id>',views.ShowDetails),
    path('Address',views.Address),
    path('Login',views.Login),
    path('Logout',views.Logout),
    path('SignUp',views.SignUp),
    path('ShowAllBookedTicket',views.ShowAllBookedTicket)
    
    
      
]
