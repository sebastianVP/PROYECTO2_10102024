from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


import datetime

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido= apellido

def sayhello(request):
    p1 = Persona("Sebastian","Valdez")
    ahora = datetime.datetime.now()
    doc_externo = loader.get_template("miplantilla.html")
    documento = doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora})
    return HttpResponse(documento)

def saludo(request):
    return HttpResponse("Bienvenido Alumnos a nuestra primera sesion en Django")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento= """
    <html>
    <body>
    <h2> 
    Fecha y hora actuales:%s
    </h2>
    </body>
    </html>
    """% fecha_actual
    return HttpResponse(documento)