from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Document


class UploadDocumentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response(
                {"error": "No file uploaded"},
                status=400
            )

        if not uploaded_file.name.endswith(
            (".txt", ".md")
        ):
            return Response(
                {
                    "error":
                    "Only .txt and .md files supported"
                },
                status=400
            )

        content = uploaded_file.read().decode(
            "utf-8"
        )

        document = Document.objects.create(
            title=uploaded_file.name,
            content={
                "type": "doc",
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": content
                            }
                        ]
                    }
                ]
            },
            owner=request.user
        )

        return Response({
            "id": document.id,
            "title": document.title
        })