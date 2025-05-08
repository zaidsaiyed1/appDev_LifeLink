from rest_framework import serializers
from core.models import *

class AmbulanceSerializer(serializers.ModelSerializer):
              class Meta:
                      model = ambulance
                      fields = "__all__"

class AmbulanceCurrentLocationSerializer(serializers.ModelSerializer):
        class Meta:
                model = ambulanceCurrentLocation
                fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
        class Meta:
                model = Notification
                fields = "__all__"