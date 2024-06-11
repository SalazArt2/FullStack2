from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import View
from .paypal_config import paypalrestsdk
from licores.models import Carrito, Licor

class VistaCrearPago(View):
    def post(self, request):
        items = []
        usuario = request.user
        carrito, created = Carrito.objects.get_or_create(usuario=usuario)
        
        for item in carrito.items.all():
            items.append({
                "name": item.licor.nombre,
                "sku": str(item.licor.id),
                "price": str(item.licor.precio),
                "currency": "MXN",
                "quantity": item.cantidad
            })

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": request.build_absolute_uri('/payment/execute/'),
                "cancel_url": request.build_absolute_uri('/payment/cancel/')
            },
            "transactions": [{
                "item_list": {
                    "items": items
                },
                "amount": {
                    "total": str(sum(item.licor.precio * item.cantidad for item in carrito.items.all())),
                    "currency": "MXN"
                },
                "description": "Compra de licor"
            }]
        })

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    return JsonResponse({'approval_url': link.href})
        else:
            return JsonResponse({'error': payment.error}, status=400)
class VistaEjecutarPago(View):
    def get(self, request):
        # Obtener los parámetros de la URL
        payment_id = request.GET.get('paymentId')
        payer_id = request.GET.get('PayerID')
        
        # Obtener el objeto de pago de PayPal
        payment = paypalrestsdk.Payment.find(payment_id)
        
        # Ejecutar el pago con el PayerID proporcionado
        if payment.execute({"payer_id": payer_id}):
            # Redirigir a la URL de éxito
            # Eliminar los objetos del carrito
            usuario = request.user
            carrito = Carrito.objects.get(usuario=usuario)
            items_en_carrito = carrito.items.all()
            for item in items_en_carrito:
                licor = item.licor
                licor.cantidad -= item.cantidad
                licor.save()
                item.delete()
            return redirect('inicio')
        #else:
            # Manejar el caso en el que el pago no se ejecutó con éxito
            # Redirigir a una página de error o hacer lo que sea necesario
            #return redirect('pagina_de_error')