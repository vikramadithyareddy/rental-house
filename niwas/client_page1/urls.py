from django.urls import path
from . import views
app_name="client_page1"
urlpatterns = [
    path('home/', views.home,name='client_page1-home'),
    path('block/', views.block,name='client_page1-block'),
    path('maps/', views.map,name='client_page1-maps'),
]
