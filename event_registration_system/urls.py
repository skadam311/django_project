
from django.contrib import admin
from django.urls import path,include
from .import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from UserApp import views as UserApp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',UserApp_views.index,name='index'),
    path('',include('UserApp.urls')),
  
     
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)