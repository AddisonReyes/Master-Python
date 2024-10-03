from django.shortcuts import HttpResponse, redirect, render

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (Metodos)
# MVT = Modelo Template Vista -> Acciones (Metodos)

layout = """
    <h1>Sitio web con Django</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Pagina de pruebas</a>
        </li>
        <li>
            <a href="/contacto">contacto</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    year: int = 2021
    years: list[str] = []
    while year <= 2050:
        if year % 2 == 0:
            years.append(str(year))
        year += 1

    nombre: str = "Addison Reyes"
    lenguajes: list[str] = ["JavaScript", "Python", "PHP", "C"]

    return render(
        request,
        "index.html",
        {
            "title": "Inicio",
            "mi_variable": "Soy un dato que esta en la vista",
            "nombre": nombre,
            "lenguajes": lenguajes,
            "years": years,
        },
    )


def hola_mundo(request):
    return render(request, "hola_mundo.html")


def pagina(request, redirigir: int = 0):
    if redirigir == 1:
        return redirect("contacto", nombre="Victor", apellidos="Robles")

    return render(request, "pagina.html")


def contacto(request, nombre: str = "", apellidos: str = ""):
    html = ""

    if nombre and apellidos:
        html += f"<p>El nombre completo es: <h3>{nombre} {apellidos}</h3></p>"
    elif nombre:
        html += f"<p>El nombre completo es: <h3>{nombre} {apellidos}</h3></p>"

    return HttpResponse(layout + "<h2>Contacto</h2>" + html)
