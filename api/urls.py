from django.urls import path
from . import views
urlpatterns = [
    path('', views.allcontact, name="allcontact"),
    path('formsubmit',views.formsubmit,name="formsubmit")
    ]