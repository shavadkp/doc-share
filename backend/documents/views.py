from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):

    serializer_class = DocumentSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Document.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DebugAuthView(APIView):
    def get(self, request):
        return Response({
            "user": str(request.user),
            "auth": str(request.auth)
        })