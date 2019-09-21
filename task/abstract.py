from django.db import models
from django.utils.translation import gettext as _


class TimestampAbstractModel(models.Model):
    """
    Holds created_at field which may turn
    out useful for every model someday.

    """
    created_at = models.DateTimeField(
        _("date created"), blank=True, auto_now_add=True
    )

    class Meta:
        abstract = True
