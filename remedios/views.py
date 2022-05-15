from django.http import Http404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

# Create your views here.

class LatestRemediosList(APIView):
    def get(self, request, format=None):
        remedios = Remedios.objects.all()[0:4]
        serializer = RemedioSerializer(remedios, many=True)
        return Response(serializer.data)

class RemediosDetail(APIView):
    def get_object(self, categoria_slug, remedio_slug):
        try:
            return Remedios.objects.filter(categoria__slug=categoria_slug).get(slug=remedio_slug)
        except Remedios.DoesNotExist:
            raise Http404
    
    def get(self, request ,categoria_slug, remedio_slug, format=None):
        remedio = self.get_object(categoria_slug, remedio_slug)
        serializer = RemedioSerializer(remedio) 

        return Response(serializer.data)

class CategoriaDetail(APIView):
    def get_object(self, categoria_slug):
        try:
            return CategoriaRemedio.objects.get(slug=categoria_slug)
        except CategoriaRemedio.DoesNotExist:
            raise Http404

    def get(self, request ,categoria_slug, format=None):
        categoria = self.get_object(categoria_slug)
        serializer = CategoriaSerializer(categoria) 

        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        remedios = Remedios.objects.filter(Q(nombreRemedio__icontains=query) | Q(descripcionRemedio__icontains=query))
        serializer = RemedioSerializer(remedios, many=True)
        return Response(serializer.data)
    else:
        return Response({"remedios": []})