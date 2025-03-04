from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Node
from .serializers import NodeSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer