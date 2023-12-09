from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import ver_perfiles, programar_cita

urlpatterns = [
    path("", TemplateView.as_view(template_name="inicio.html"), name="inicio"),

    path("inicio_sesion/", views.inicio_sesion, name="inicio_sesion"),

    path('pagina_ayuda_soporte/', views.AyudaSoporte, name='pagina_ayuda_soporte'),

    path('pagina_registro/', views.PaginaRegistro, name='pagina_registro'),

    path('error_page/', views.error_page, name='error_page'),

    path('ver_perfiles/', ver_perfiles, name='ver_perfiles'),

    path('programar_cita/', programar_cita, name='programar_cita'),
]