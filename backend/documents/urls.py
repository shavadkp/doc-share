from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import DocumentViewSet
from .upload_views import UploadDocumentView

router = DefaultRouter()
router.register('', DocumentViewSet, basename='documents')

urlpatterns = [
    path(
        'upload/',
        UploadDocumentView.as_view(),
        name='upload-document'
    ),
]

urlpatterns += router.urls