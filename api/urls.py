from django.urls import path
from . import views
urlpatterns = [
    path('', views.allcontact, name="allcontact"),
    path('formsubmit',views.formsubmit,name="formsubmit"),
    path('detailContact/<str:pk>/',views.detailContact,name="detailContact"),
    path('deleteContact/<str:pk>/',views.deleteContact,name="deleteContact")
    ]