from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from documents.models import Document

class SharedDocument(models.Model):

    VIEWER = "viewer"
    EDITOR = "editor"

    PERMISSIONS = [
        (VIEWER, "Viewer"),
        (EDITOR, "Editor")
    ]

    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    permission = models.CharField(
        max_length=20,
        choices=PERMISSIONS,
        default=VIEWER
    )

    class Meta:
        unique_together = ("document", "user")