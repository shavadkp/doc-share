from django.urls import path
from .views import ShareDocumentView

urlpatterns = [
    path(
        '<int:doc_id>/share/',
        ShareDocumentView.as_view()
    )
]