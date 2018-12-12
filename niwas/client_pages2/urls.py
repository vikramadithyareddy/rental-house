from django.urls import re_path, include, path
from . import views
app_name="client_pages2"
urlpatterns = [
    path('home/<int:id>' , views.home , name='home'),
    path('feedback/<int:id>' , views.feedback , name='feedback'),
]
