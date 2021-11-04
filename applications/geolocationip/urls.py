from django.urls import path
from . import views

app_name= 'ip_app'

urlpatterns = [
    #path('',views.GetIpTracker.as_view(),name='home'),
    path('',views.get_ip_tracker,name='ip_tracker'),
]
