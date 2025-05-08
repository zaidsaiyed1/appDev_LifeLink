from rest_framework import routers
from core import views
from django.urls import path,include


urlpatterns = [
              path('get-currentlocation/',views.get_CurrentLocationAmbulance,name="get-currentlocation"),
              path('ambulanceCurrentLocations/',views.AmbulanceCurrentLocationApi.as_view()),
              path('notifications/',views.NotificationApi.as_view()),
             
]