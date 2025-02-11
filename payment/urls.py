

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PaymentViewSet

# Initialize the router
router = DefaultRouter()
router.register('checkout', views.CheckoutViewSet)
router.register(r'payment', PaymentViewSet, basename='payment')

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)), 
    path('payment/success/', views.PaymentSuccessAPI.as_view(), name='payment_success'),  # URL for successful payment
    path('payment/failed/', views.PaymentFailedAPI.as_view(), name='payment_failed'),  # URL for failed payment
    path('payment/cancel/', views.PaymentCancelAPI.as_view(), name='payment_cancel'),  # URL for canceled payment
]

