from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template.loader import get_template
from django.shortcuts import render
# a cada funcion creada en el archivo views se le denomina 'VISTA'


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    nombre = 'Jorge'
    apellido = 'Febres'
    p1 = Persona(nombre, apellido)
    fecha = datetime.datetime.now()
    temas = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    # doc_externo = open(
    #     'C:/Users/jorge/Documents/GitHub/django pildoras tutorial/Proyecto1/Proyecto1/templates/mitemplate.html')
    # mi_template = Template(doc_externo.read())
    # documento = mi_template.render(mi_contexto)
    # return HttpResponse(documento)
    # mi_contexto = Context(
    #     {'p1': p1, 'fecha': fecha, 'temas': temas})
    # utilizando el loader:
    # mi_contexto = Context(
    #     {'nombre': nombre, 'apellido': apellido, 'fecha': fecha})
    # doc_externo.close()

    # nuevos coments
    # doc_externo = get_template('mitemplate.html')
    # documento = doc_externo.render({'p1': p1, 'fecha': fecha, 'temas': temas})
    return render(request, "mitemplate.html", {'p1': p1, 'fecha': fecha, 'temas': temas})


def despedida(request):
    return HttpResponse('Saliendo de la primera página con django')


def getFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = '''
    <html>
        <div>
            <h1>
                Fecha y Hora: %s
            </h1>
        </div>
    </html>
    ''' % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request, anio, edad):
    edadActual = edad
    periodo = anio - 2020
    edadFutura = edadActual + periodo

    documento = '''
    <html>
        <body>
            <div>
                <h1>
                    En el año: %s, tendrás: %s años
                </h1>
            </div>
        </body>
    </html>
    ''' % (anio, edadFutura)
    return HttpResponse(documento)


def curso_c(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'cursoC.html', {'dame_fecha': fecha_actual})


def curso_css(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'cursoCss.html', {'dame_fecha': fecha_actual})
