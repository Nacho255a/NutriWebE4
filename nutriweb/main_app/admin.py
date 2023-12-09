from django.contrib import admin
from .models import (
    Clientes,
    Nutricionistas,
    Dietistas,
    Citas,
    EvaluacionesNutricionales,
    UsuariosDelSistema,
    Alimentos,
    Dietas,
    HistorialMedico,
    DietasAlimentos,
)

admin.site.register(Clientes)
admin.site.register(Nutricionistas)
admin.site.register(Dietistas)
admin.site.register(Citas)
admin.site.register(EvaluacionesNutricionales)
admin.site.register(UsuariosDelSistema)
admin.site.register(Alimentos)
admin.site.register(Dietas)
admin.site.register(HistorialMedico)
admin.site.register(DietasAlimentos)