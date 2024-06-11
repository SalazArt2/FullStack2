from django.urls import path

from .views import VistaPaginaRegistro
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

urlpatterns = [
    path( 'signup/', VistaPaginaRegistro.as_view(), name='signup' ),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]