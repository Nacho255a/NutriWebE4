from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, ProgramarCitaForm
from .models import Clientes, UsuariosDelSistema, Citas
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Registro de usuarios
def PaginaRegistro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            tipo_usuario = form.cleaned_data.get("TipoUsuario")
            if tipo_usuario == "Cliente":
                cliente = Clientes.objects.create(
                    RutCliente=user.username,
                    Nombre=form.cleaned_data.get("first_name"),
                    Apellido=form.cleaned_data.get("last_name"),
                    Email=form.cleaned_data.get("email"),
                )
                UsuariosDelSistema.objects.create(
                    Username=user.username, TipoUsuario=tipo_usuario, RutCliente=cliente
                )
            elif tipo_usuario == "Nutricionista":
                # Similar para otros tipos de usuarios
                pass

            return render(request, "ver_perfiles.html", {"user": user})
    else:
        form = RegistroUsuarioForm()

    return render(request, "pagina_registro.html", {"form": form})


# Inicio de sesión
def inicio_sesion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(
                request, "ver_perfiles.html", {"user": user}
            )  # Redirige a la página principal después del inicio de sesión
        else:
            # Agrega un mensaje de error para mostrar en el formulario
            return render(
                request,
                "error_page.html",
                {
                    "error_message": "Credenciales inválidas. Por favor, inténtalo de nuevo."
                },
            )
    return render(request, "inicio_sesion.html")


def programar_cita(request):
    if request.method == "POST":
        form = ProgramarCitaForm(request.POST)
        if form.is_valid():
            # Guardar la cita en la base de datos
            cita = form.save()
            return redirect("ver_perfiles")
    else:
        form = ProgramarCitaForm()

    return render(request, "programar_cita.html", {"form": form})


# Visualización de Perfiles de Clientes
@login_required
def ver_perfiles(request):
    perfiles = Clientes.objects.all()
    return render(request, "ver_perfiles.html", {"perfiles": perfiles})


# Pagina De Error
def error_page(request):
    error_message = "Ocurrió un error inesperado."
    return render(request, "error_page.html", {"error_message": error_message})


def AyudaSoporte(request):
    return render(request, "pagina_ayuda_soporte.html")
