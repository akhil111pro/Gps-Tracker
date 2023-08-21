from django.urls import path
from . import views

urlpatterns = [ 
               
    path('', views.index, name='index'),
    path('map/' , views.map_view , name='map'),
    path('endpoint/',views.handle_post_request , name='endpoint'),
    path('updatedata/' , views.updatedata , name= 'updatedata')
     
] 