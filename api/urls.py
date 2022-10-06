from django.urls import path
from . import views
urlpatterns = [
    path('', views.allcontact, name="allcontact"),
    path('formsubmit',views.formsubmit,name="formsubmit"),
    path('<str:pk>/',views.detailContact,name="detailContact"),
    path('deleteContact/<str:pk>/',views.deleteContact,name="deleteContact"),
    path('updateContact/<str:pk>/',views.updateContact,name="updateContact")
    ]