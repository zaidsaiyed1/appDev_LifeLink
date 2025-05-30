from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
   path('register/',views.register,name='register'),
   path('editProfile/<str:email>/',views.editdata,name='editProfile'),
   path('registerForManager/',views.registerForManager,name='registerForManager'),
   path('login/',views.loginhandle,name='login'),
   path('profile/<str:email>/',views.profileData,name='profile'),
   path('editdata/<str:email>/',views.editdata,name='editdata'),
   path('conformUserDelete/<str:email>/',views.comformUserDelete,name='conformUserDelete'),
   path('deleteUser/<str:email>/',views.deleteUser,name='deleteUser'),
   path('logout/',views.logouthandle,name='logout'),
   path('token/',TokenObtainPairView.as_view(),name="token"),
   path('token/refresh/',TokenRefreshView.as_view(),name="refresh")
]