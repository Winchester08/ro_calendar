from django.shortcuts import HttpResponse, render
from .models import usuarios
from django.db import connection


def login(request):
    titulo = 'Login de Usuarios'
    sistema = 'Calendario de Eventos'
    return render (request, 'login/login.html', {
        'ventana' : titulo,
        'sistema': sistema
    })

def valida_usuarios(request):
    
    mensaje1 = 'Usuario Aceptado'
    mensaje2 = 'Existe un error en los datos verifique'
    sistema = 'Calendario de Eventos'

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')

        u = usuarios.objects.filter(usuario = usuario, clave=clave)
       
        print ("Usuario:",u)
        

        if (u == usuario ): 
            return HttpResponse (mensaje1)
        else :
            return HttpResponse (mensaje2)
           

def interfaz_admin(request):
    titulo = 'Interfaz Principal'
    sistema = 'Calendario de Eventos'
    return render (request, 'calendario/interfazp.html', {
        'ventana' : titulo,
        'sistema': sistema
    })

def interfaz_users(request):
    titulo = 'Interfaz Usuarios'
    sistema = 'Calendario de Eventos'

    consulta_eventos = """ Select * from calendario_evento where estado ='en proceso' order 
    by fecha desc """
    with connection.cursor() as cursor:
        cursor.execute(consulta_eventos)
        columns = [col[0] for col in cursor.description]
        resultado = [dict(zip(columns, row)) for row in cursor.fetchall()]

    #aqui hay que hacer la consulta para que nos muestre el detalle de eventos
    return render (request, 'calendario/interfazu.html', {
        'ventana' : titulo,
        'sistema': sistema,
        'datos': resultado
    })