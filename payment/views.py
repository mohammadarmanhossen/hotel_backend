from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
import uuid
from sslcommerz_lib import SSLCOMMERZ
from .serializer import CheckoutSerializers
from .models import Checkout,Booked
from django.shortcuts import redirect
from .import views
from rest_framework.permissions import AllowAny


class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializers

class PaymentViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def create_payment(self, request):

        user_id = request.data.get('user')
        total_amount = request.data.get('total_amount')
        hotelId = request.data.get('hotelId')

        user = None
        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"error": "Invalid user ID"}, status=400)

        tran_id = str(uuid.uuid4())[:10]

        settings = {
            'store_id': 'arman679a8128a9e35',
            'store_pass': 'arman679a8128a9e35@ssl',
            'issandbox': True,
        }

        sslcz = SSLCOMMERZ(settings)

        post_body = {
            'total_amount': total_amount,
            'currency': "BDT",
            'tran_id': tran_id,
            'success_url': f"http://127.0.0.1:8000/payment/success/{hotelId}/",
            'fail_url': "http://127.0.0.1:8000/payment/failed/",
            'cancel_url': "http://127.0.0.1:8000/payment/cancel/",
            'emi_option': 0,
            'cus_name': "arman",
            'cus_email': "arman@gmail.com",
            'cus_phone': "1908349238",
            'cus_add1': "Mirpur, Dhaka",
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "10304040",
            'num_of_item': 1,
            'product_name': "Test Product",
            'product_category': "Test Category",
            'product_profile': "general",
        }

        try:
            response = sslcz.createSession(post_body)
            if 'GatewayPageURL' not in response:
                return Response({"error": "Payment session creation failed", "details": response}, status=400)
            return Response({'payment_url': response['GatewayPageURL']})
        except Exception as e:
            return Response({"error": "Payment processing failed", "details": str(e)}, status=500)


class PaymentSuccessAPI(APIView):

    def post(self,request,hotelId):

        booked = Booked.objects.filter(id=hotelId ).first()

        if booked:
            booked.is_paid = True
            booked.save()
            return redirect("http://127.0.0.1:5502/user_dashboard.html")

        return Response({"error": "Booking not found"}, status=404)

class PaymentFailedAPI(APIView):


    def post(self, request):
        return redirect("http://127.0.0.1:5502/user_dashboard.html")


class PaymentCancelAPI(APIView):
 
    def post(self, request):
        return redirect("http://127.0.0.1:5502/user_dashboard.html")





