from rest_framework import routers
from core import views
from django.urls import path,include


urlpatterns = [
              path('get-currentlocation/',views.get_CurrentLocationAmbulance,name="get-currentlocation"),
              path('ambulanceCurrentLocations/',views.AmbulanceCurrentLocationApi.as_view()),
              path('notifications/',views.NotificationApi.as_view()),
              path('user/',views.CustomUserApi.as_view()),
              path('ambulances/',views.AmbulancesApi.as_view()),
              path('LoginUserView/',views.UserLoginView.as_view()),
              path('getUserAmbulance/',views.UserAmbulancesApi.as_view()),
             
]