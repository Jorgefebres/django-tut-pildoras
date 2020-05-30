from django.shortcuts import render
from django.http import HttpResponse
from gestion_pedidos.models import Articulo
from django.core.mail import send_mail
from django.conf import settings
from gestion_pedidos.forms import formulario_contacto
# Create your views here.


def busqueda_producto(request):
    return render(request, "busqueda_producto.html")


def retorna_producto(request):
    if request.GET['text_search_product']:
        productoBuscado = request.GET['text_search_product']
        if len(productoBuscado) > 20:
            mensaje = 'Introduce un criterio mas corto (menor a 20 caracteres) para buscar productos'
        else:
            # icontains funciona como un ilike
            productos = Articulo.objects.filter(
                nombre__icontains=productoBuscado)
            return render(request, 'resultados_busqueda.html', {'productos': productos, 'query': productoBuscado})
    else:
        mensaje = 'No has introducido ningun criterio para buscar productos'
    return HttpResponse(mensaje)


def contactar(request):
    # if request.method == 'POST':
    #     subject = request.POST['asunto']
    #     message = request.POST['mensaje'] + ' ' + request.POST['email']
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list = ['joradfebres@gmail.com']
    #     send_mail(subject, message, email_from, recipient_list)
    #     return render(request, "gracias.html")

    if request.method == 'POST':
        mi_form = formulario_contacto(request.POST)
        if mi_form.is_valid():
            form_data = mi_form.cleaned_data
            send_mail(form_data['asunto'], form_data['mensaje'],
                      form_data.get('email', ''), ['jorge_febres@outlook.com'],)
            return render(request, 'gracias.html')
    else:
        mi_form = formulario_contacto()

    return render(request, 'formulario_contacto.html', {'form': mi_form})
