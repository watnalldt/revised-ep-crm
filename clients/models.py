from django.db import models
from simple_history.models import HistoricalRecords

from core.models import TimeStampedModel
from users.models import AccountManager


class ClientsManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related(
                "account_manager",
            )
        )


class Client(TimeStampedModel):
    client = models.CharField(verbose_name="Client", max_length=255, unique=True)
    account_manager = models.ForeignKey(
        AccountManager,
        on_delete=models.CASCADE,
        verbose_name="Account Manager",
        related_name="account_manager_clients",
    )
    history = HistoricalRecords()

    objects = ClientsManager()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["client"]

    def __str__(self):
        return self.client
