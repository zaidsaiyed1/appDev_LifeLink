from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns= [
path('',views.home,name='index'),
path('registerAmbulance/',views.addAmbulance,name="registerAmbulance"),
path('editAmbulance/<int:pk>/',views.editAmbulance,name="registerAmbulance"),
path('conformAmbulance/<int:pk>/',views.conformationToDeleteAmbulance,name="conformAmbulance"),
path('deleteAmbulance/<int:pk>/',views.deleteAmbulance,name="deleteAmbulance"),
              
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)