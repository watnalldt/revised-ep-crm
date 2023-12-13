import pytest
from django.test import TestCase

from clients.models import Client, ClientsManager
from core.models import TimeStampedModel
from users.models import AccountManager


@pytest.mark.django_db
class TestClientModel(TestCase):
    def setUp(self):
        self.account_manager = AccountManager.objects.create(email="test@email.com")
        self.client = Client.objects.create(
            client="Test Client",
            account_manager=self.account_manager,
        )

    def test_client_model(self):
        # Retrieve the client from the database
        client_from_db = Client.objects.get(client="Test Client")

        # Check if the client was created correctly
        self.assertEqual(client_from_db.client, "Test Client")
        self.assertEqual(client_from_db.account_manager, self.account_manager)

    def test_client_str_representation(self):
        # Ensure that the __str__ method returns the client name
        self.assertEqual(str(self.client), "Test Client")
