import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def pago(request):
    serializer = OrdenSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        monto_pago = sum(item.get('cantidad') * item.get('items').precio for item in serializer.validated_data['items'])

        try:
            cobro = stripe.Charge.create(
                amount=int(monto_pago * 100),
                currency='USD',
                description="Cobro de remedios",
                source=serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, monto_pago=monto_pago)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)