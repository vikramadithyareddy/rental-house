from django.conf.urls import url
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'client'

urlpatterns = [

        url(r'^bookRoom/(?P<id>[0-9]+)$', views.bookRoom, name='bookRoom'),
        url(r'^bookHostel/(?P<id>[0-9]+)$', views.bookHostel , name='bookHostel'),
        url(r'^booking_house/(?P<id>[0-9]+)$', views.store_data_house, name='booking_house'),
        url(r'^booking_hostel/(?P<id>[0-9]+)$', views.store_data_hostel, name='booking_hostel'),
        url(r'^cancel_booking_house/(?P<id>[0-9]+)$', views.cancelbooking_house, name='house_cancelbooking'),
        url(r'^cancel_booking_hostel/(?P<id>[0-9]+)$', views.cancelbooking_hostel, name='hostel_cancelbooking'),
        url(r'^viewbookings/$', views.mybookings , name='viewbookings'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)