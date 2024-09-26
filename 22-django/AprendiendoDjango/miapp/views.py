from django.shortcuts import HttpResponse, render

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
        <h1>Inicio</h1>
        <p>Años hasta el 2050</p>
        <ul>
    """

    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    return HttpResponse(layout + html)


def hola_mundo(request):
    return HttpResponse(
        layout
        + """
        <h1>Hola mundo con Django!!</h1>
        <h3>Soy Addison Reyes</h3>
        """
    )


def pagina(request):
    return HttpResponse(
        layout
        + """
        <h1>Pagina de mi web</h1>
        <p>Creado por Addison Reyes</p>
        """
    )


def contacto(request, nombre):
    return HttpResponse(
        layout
        + f"""
        <h2>Contacto {nombre}</h2>
        """
    )
