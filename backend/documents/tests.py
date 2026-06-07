from django.contrib.auth.models import User
from documents.models import Document
from sharing.models import SharedDocument

class SharingTest(TestCase):

    def test_share_document(self):

        owner = User.objects.create_user(
            username="alice"
        )

        viewer = User.objects.create_user(
            username="bob"
        )

        document = Document.objects.create(
            title="Shared Doc",
            owner=owner,
            content={"type": "doc"}
        )

        shared = SharedDocument.objects.create(
            document=document,
            user=viewer,
            permission="viewer"
        )

        self.assertEqual(
            shared.user.username,
            "bob"
        )