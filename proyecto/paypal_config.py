import paypalrestsdk # type: ignore
from django.conf import settings

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # sandbox o live
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})