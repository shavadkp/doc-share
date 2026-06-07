from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SharedDocument

from documents.models import Document

class ShareDocumentView(APIView):

    def post(self, request, doc_id):

        email = request.data.get("email")

        permission = request.data.get(
            "permission",
            "viewer"
        )

        document = Document.objects.get(
            id=doc_id,
            owner=request.user
        )

        user = User.objects.get(
            email=email
        )

        SharedDocument.objects.update_or_create(
            document=document,
            user=user,
            defaults={
                "permission": permission
            }
        )

        return Response(
            {"message": "shared"}
        )
    
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from documents.models import Document
from .models import SharedDocument


class ShareDocumentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, doc_id):

        email = request.data.get("email")

        permission = request.data.get(
            "permission",
            "viewer"
        )

        document = Document.objects.get(
            id=doc_id,
            owner=request.user
        )

        user = User.objects.get(
            email=email
        )

        SharedDocument.objects.update_or_create(
            document=document,
            user=user,
            defaults={
                "permission": permission
            }
        )

        return Response({
            "message": "Document shared"
        })