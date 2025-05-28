from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ambulance)
admin.site.register(routeAmbulance)
admin.site.register(ambulanceCurrentLocation)
admin.site.register(Notification)
admin.site.register(ambulanceOrgaDetail)