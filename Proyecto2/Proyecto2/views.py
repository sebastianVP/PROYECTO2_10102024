from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Bienvenido Alumnos a nuestra primera sesion en Django")