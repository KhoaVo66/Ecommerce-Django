from django.urls import path
from . import views

urlpatterns = [
    path('payment_card', views.payment_card, name='payment_card'),
    path('process_payment', views.process_payment, name='process_payment'),
    path('checkout', views.checkout, name='checkout'),
    path('billing', views.billing, name="billing")
]