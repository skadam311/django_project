from django.db import models

# Create your models here.
class Category(models.Model):
    event_type= models.CharField(max_length=100)
    
    def __str__(self):
        return self.event_type
    
    class Meta:
        db_table="Category"
        
class EventList(models.Model):   
    Event_name = models.CharField(max_length=100)
    event_image=models.ImageField(default="abc.jpg",upload_to="images")
    Date = models.DateTimeField(blank=True,null=True )
    start_Time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    mobile = models.CharField(max_length=15)
    Website = models.CharField(max_length = 50)
    address = models.CharField(max_length=500,null=True)
    ticekt_amount = models.IntegerField(default=200, null=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.Event_name
    
    
    
    class Meta:
        db_table ="event_list"
