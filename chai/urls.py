from django.urls import path
from . import views
urlpatterns = [
    path('hello', views.all_chai_requests, name= 'all_chai'),
    path('', views.all_chai_requests, name= 'all_chai')

]
