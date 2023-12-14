import pytest
from django.test import TestCase
from django.db import IntegrityError
from clients.models import Client
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

    def test_unique_client(self):
        # Test that the 'client' field is unique
        account_manager = AccountManager.objects.create(email="test@example.com")
        Client.objects.create(client="Test Client1", account_manager=account_manager)

        with pytest.raises(IntegrityError):
            Client.objects.create(client="Test Client1", account_manager=account_manager)

    def test_manager_select_related(self):
        # Test the custom manager's select_related behavior
        account_manager = AccountManager.objects.create(email="test@example.com")
        client = Client.objects.create(client="Test Client2", account_manager=account_manager)

        # Retrieve the client using the manager's queryset
        client_from_manager = Client.objects.get(client="Test Client2")

        # Ensure that the account_manager is fetched via select_related
        assert client_from_manager.account_manager == account_manager
