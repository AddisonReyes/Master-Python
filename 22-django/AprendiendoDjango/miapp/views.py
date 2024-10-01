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

    html = """
        
    """

    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    return render(request, "index.html")
    return HttpResponse(layout + html)


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
