from django.shortcuts import render

def nuevo_calendario(request):
    titulo = 'Nuevo Evento'
    sistema = 'Calendario de Eventos'
    return render(request, 'calendario/nuevo_calendario.html',{
        'sistema':  sistema,
        'ventana':  titulo
    })
