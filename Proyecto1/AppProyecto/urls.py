from django.urls import path
from AppProyecto import views 

urlpatterns = [
        path('', views.Inicio, name="inicio"),
]