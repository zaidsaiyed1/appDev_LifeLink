from rest_framework import serializers
from core.models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import settings
# from django.conf import settings
from accounts.models import CustomUser

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

class CustomUserSerializer(serializers.ModelSerializer):
        token = serializers.SerializerMethodField()
        
        # def get_token(self,obj):
        #         jwt_payload_handler = settings.JWT_PAYLOAD_HANDLER
        #         jwt_encoded_handler  = settings.JWT_ENCODED_HANDLER
        #         payload = jwt_payload_handler(obj)
        #         token = jwt_encoded_handler(payload)
        #         return token
        def create(self, validated_data):
             password = validated_data.pop("password", None)
             user = CustomUser(**validated_data)
             if password:
                   user.set_password(password)
             user.save()
             return user
        def get_token(self, obj):
             refresh = RefreshToken.for_user(obj)
             return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
                }

        class Meta:
                model = CustomUser
                fields = ["id","email","password","number","is_driver","is_ambulanceOrganizer_Person","token"]
                extra_kwargs = {"password":{"write_only":True}}