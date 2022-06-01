from django.contrib import admin
from AdminApp.models import Category,EventList

class CategoryAdmin(admin.ModelAdmin):
    list_diplay=("id","event_type")
    
class EventListAdmin(admin.ModelAdmin):
    list_diplay=("id","Event_name","event_image","Date","Time","connect_person","mobile","website","addres","ticket_amount")
admin.site.register(Category,CategoryAdmin)
admin.site.register(EventList,EventListAdmin)