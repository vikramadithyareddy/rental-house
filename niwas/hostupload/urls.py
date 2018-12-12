from django.urls import path
from hostupload import views

app_name = 'hostupload'

urlpatterns = [
    path('host/',views.UploadFormview,name='host'),
    path('hostel/',views.UploadHostelview,name='hostel'),
    path('house/',views.UploadHouseview,name='house'),

]
