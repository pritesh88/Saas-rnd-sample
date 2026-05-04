
from django.urls import path

from . import views 

urlpatterns = [
    
   path("",views.profiles_list_view), 
   path("<str:username>/", views.profile_view),
]
