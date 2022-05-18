from django.shortcuts import render, redirect
from email import message
from django.conf import settings
from django.core.mail import send_mail

from django.conf import settings
from django.http import Http404, JsonResponse
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import correoSerializer
from .models import correoCliente

# Create your views here.

@api_view(['POST'])
def enviarCorreo(request):
    serializer = correoSerializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save()

            print(serializer)

            return JsonResponse(serializer.data)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('full-name')
        correo = request.POST.get('email')
        asunto = request.POST.get('subject')
        mensaje = request.POST.get('message')

        data= {
            'nombre' : nombre,
            'email' : correo,
            'telefono' : telefono,
            'subject' : asunto,
            'message' : mensaje

        }
        message = '''
        New message: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '',['matideus74@gmail.com'])

    return render(request, 'core/contacto.html')"""