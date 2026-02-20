from django.shortcuts import render, HttpResponse
from datetime import date
from .models import evento

def nuevo_calendario(request):
    titulo = 'Nuevo Evento'
    sistema = 'Calendario de Eventos'
    return render(request, 'calendario/nuevo_calendario.html',{
        'sistema':  sistema,
        'ventana':  titulo
    })

def guarda_evento(request):
    mensaje = 'Evento guardado con exito'
    sistema = 'Calendario de Eventos'
    if request.method == "POST":
        f = date.today()
        f1 = '{}-{}-{}'.format(f.year,f.month, f.day)
        fecha = f1
        dia_evento = request.POST.get('dia')
        des = request.POST.get('desc')
        hora = request.POST.get('hora')
        estatus = request.POST.get('estatus')
        guarda = evento(fecha=fecha, hora=hora, descripcion=des, estado=estatus)
        guarda.save()
        print ("Datos Guardados")
        #return HttpResponse("Guardado con Exito")
        return render(request, "calendario/mensaje.html", {
            'aviso':    mensaje,
            'sistema':  sistema
        })

    else:
        print("Existe un error en el guardado, verifica")
        return HttpResponse("Guardado no realizado")
