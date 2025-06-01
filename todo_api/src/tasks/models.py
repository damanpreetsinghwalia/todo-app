from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy


class Item(models.Model):
    class Status(models.IntegerChoices):
        TODO = 1, gettext_lazy("Todo")
        WIP = 2, gettext_lazy("Work in Progress")
        DONE = 3, gettext_lazy("Done")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        related_name="items",
        verbose_name=gettext_lazy("User"),
    )
    text = models.CharField(gettext_lazy("Text"), max_length=255)
    status = models.PositiveSmallIntegerField(
        gettext_lazy("Status"), choices=Status.choices, default=Status.TODO
    )
    created = models.DateTimeField(gettext_lazy("Created At"), auto_now_add=True)
    updated = models.DateTimeField(gettext_lazy("Updated At"), auto_now=True)

    class Meta:
        verbose_name = gettext_lazy("Item")
        verbose_name_plural = gettext_lazy("Items")
