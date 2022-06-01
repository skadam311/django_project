
from django.db import models
from AdminApp.models import EventList

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    
    

    class Meta:
        db_table = "UserDetails"
        
        
class BookEvent(models.Model):
    user = models.ForeignKey(UserDetails, null=True, on_delete=models.CASCADE)
    event= models.ForeignKey(EventList,on_delete=models.CASCADE)
    person=models.IntegerField()  
    class Meta:
        db_table="BookEvent"

