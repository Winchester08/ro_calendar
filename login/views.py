from django.shortcuts import HttpResponse, render
from .models import usuarios


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
    return render (request, 'calendario/interfazu.html', {
        'ventana' : titulo,
        'sistema': sistema
    })