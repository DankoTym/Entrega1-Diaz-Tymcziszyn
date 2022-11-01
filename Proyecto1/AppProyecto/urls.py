from django.urls import path
from AppProyecto import views 

urlpatterns = [
        path('', views.Inicio, name="inicio"),
        #Formularios de Carga:
        path('productosFormulario/', views.productosFormulario, name="productosFormulario"),
        path('contactoFormulario/', views.contactoFormulario, name="contactoFormulario"),
        path('clientesFormulario/', views.clientesFormulario, name="clientesFormulario"),
        #Formularios de Busqueda:
]