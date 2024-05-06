from django.urls import path
from Home import views 
# In your Django app's urls.py file
from django.urls import path
urlpatterns = [
    path("",views.index,name="Home" ),
    path('contact',views.contact,name="contact"),
    path('photos',views.photos,name="photos"),
    path('teachers',views.teachers,name="teacher"),
]