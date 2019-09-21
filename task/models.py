from task.abstract import TimestampAbstractModel
from django.db import models


class Subscriber(TimestampAbstractModel):

    email = models.EmailField(unique=True, blank=True, null=True)
    gdpr_consent = models.BooleanField(default=False)


class SubscriberSMS(TimestampAbstractModel):
    phone = models.CharField(blank=True, null=True, max_length=12)
    gdpr_consent = models.BooleanField(default=False)


class Client(TimestampAbstractModel):
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(blank=True, null=True,  max_length=12)


class User(TimestampAbstractModel):
    email = models.EmailField(unique=True, blank=True, null=True)
    # i am aware this should be validated in some way but in fact
    # it's quite out of scope in this case
    phone = models.CharField(blank=True, null=True,  max_length=12)
    gdpr_consent = models.BooleanField(default=False)
