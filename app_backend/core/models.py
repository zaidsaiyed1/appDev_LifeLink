from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
# Create your models here.


class ambulance(models.Model):
     amid = models.BigAutoField(primary_key=True)
     ambulanceName = models.CharField(max_length=100,null=False)
     ambulanceNumber = models.CharField(max_length=20,null=False,unique=True)
     ambulanceOrgaName = models.CharField(max_length=50,null=False)
     ambulanceDriverName = models.CharField(max_length=60,null=False)
     ambulanceDriver2Name = models.CharField(max_length=60,null=True)
     ambulanceDriverNum = models.IntegerField(null=False)
     ambulanceDriver2Num = models.IntegerField(null=True)
     def __str__(self):
          return f" {self.ambulanceName},{self.ambulanceNumber}" 
              

class routeAmbulance(models.Model):
     routAmb = models.BigAutoField(primary_key=True)
     ambulanceName = models.ForeignKey(ambulance,on_delete=models.CASCADE)
     fromDesti = models.CharField(max_length=100,null=False)
     toDesti = models.CharField(max_length=100,null=False)
     created_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return f"{self.ambulanceName}"
     

class ambulanceCurrentLocation(models.Model):
     curAmb = models.BigAutoField(primary_key=True)
     ambulanceName = models.ForeignKey(ambulance,on_delete=models.CASCADE)
     currLat = models.FloatField(null=False)
     currLon = models.FloatField(null=False)
     current_Address = models.CharField(max_length=200,null=False)
     created_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return f"{self.currLat},{self.currLon}"
     
class Notification(models.Model):
     notid = models.BigAutoField(primary_key=True)
     ambulanceName  = models.ForeignKey(ambulance,on_delete=models.CASCADE)
     ambulanceCurrLoc = models.ForeignKey(ambulanceCurrentLocation,on_delete=models.CASCADE)
     notification_title = models.CharField(max_length=100,null=False)
     notify_at = models.DateTimeField(auto_now_add=True)
     is_seen = models.BooleanField(default=False)
     def __str__(self):
          return f"{self.notification_title}"
     
     def save(self,*args,**kwars):
          channel_layer = get_channel_layer()
          # notification = Notification.objects.filter(is_seen=False).count()
          super(Notification,self).save(*args,**kwars)
          data = {
        'notification_title': self.notification_title,
        'ambulanceData': {
            'ambulanceName': self.ambulanceName.ambulanceName,
            'ambulanceNumber': self.ambulanceName.ambulanceNumber,
            'ambulanceOrgaName': self.ambulanceName.ambulanceOrgaName,
            'ambulanceDriverName': self.ambulanceName.ambulanceDriverName,
            'ambulanceDriver2Name': self.ambulanceName.ambulanceDriver2Name,
            'ambulanceDriverNum': self.ambulanceName.ambulanceDriverNum,
            'ambulanceDriver2Num': self.ambulanceName.ambulanceDriver2Num,
        },
        'ambulanceCurrentLoc': {
            'currLat': self.ambulanceCurrLoc.currLat,
            'currLon': self.ambulanceCurrLoc.currLon,
            'current_Address': self.ambulanceCurrLoc.current_Address,
        },
        'notify_at': self.notify_at.strftime('%Y-%m-%d %H:%M:%S'),  # If you want time also
    }
          async_to_sync(channel_layer.group_send)(
               'test_consumer_group',{
                    'type':'notify_message',
                    'message':json.dumps(data)
               }
          )

