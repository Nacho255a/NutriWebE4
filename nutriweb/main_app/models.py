from django.db import models


class Clientes(models.Model):
    RutCliente = models.CharField(max_length=12, primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    FechaNacimiento = models.DateField()
    Email = models.EmailField()
    Telefono = models.CharField(max_length=15)
    Direccion = models.CharField(max_length=100)


class Nutricionistas(models.Model):
    RutNutricionista = models.CharField(max_length=12, primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Email = models.EmailField()
    Telefono = models.CharField(max_length=15)
    Especialidad = models.CharField(max_length=50)


class Dietistas(models.Model):
    RutDietista = models.CharField(max_length=12, primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Email = models.EmailField()
    Telefono = models.CharField(max_length=15)
    Especialidad = models.CharField(max_length=50)


class Citas(models.Model):
    IDCita = models.AutoField(primary_key=True)
    RutCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    RutNutricionista = models.ForeignKey(Nutricionistas, on_delete=models.CASCADE)
    FechaCita = models.DateField()
    HoraCita = models.TimeField()
    LugarCita = models.CharField(max_length=100)


class EvaluacionesNutricionales(models.Model):
    IDEvaluacion = models.AutoField(primary_key=True)
    RutCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    RutNutricionista = models.ForeignKey(Nutricionistas, on_delete=models.CASCADE)
    FechaEvaluacion = models.DateField()
    Peso = models.FloatField()
    Altura = models.FloatField()
    IMC = models.FloatField()


class UsuariosDelSistema(models.Model):
    IDUsuario = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=255)
    TIPO_USUARIO_CHOICES = (
        ("Cliente", "Cliente"),
        ("Nutricionista", "Nutricionista"),
        ("Dietista", "Dietista"),
    )
    TipoUsuario = models.CharField(max_length=15, choices=TIPO_USUARIO_CHOICES)
    RutCliente = models.ForeignKey(
        Clientes, on_delete=models.CASCADE, blank=True, null=True
    )
    RutNutricionista = models.ForeignKey(
        Nutricionistas, on_delete=models.CASCADE, blank=True, null=True
    )
    RutDietista = models.ForeignKey(
        Dietistas, on_delete=models.CASCADE, blank=True, null=True
    )


class Alimentos(models.Model):
    IDAlimento = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()


class Dietas(models.Model):
    IDDieta = models.AutoField(primary_key=True)
    RutCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()


class HistorialMedico(models.Model):
    IDConsulta = models.AutoField(primary_key=True)
    RutCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    FechaAtencion = models.DateField()
    DescripcionConsulta = models.TextField()


class DietasAlimentos(models.Model):
    IDDieta = models.ForeignKey(Dietas, on_delete=models.CASCADE)
    IDAlimento = models.ForeignKey(Alimentos, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("IDDieta", "IDAlimento")
