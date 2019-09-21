from task.models import Client, Subscriber, SubscriberSMS, User
from django.db import IntegrityError
from django.core.management.base import BaseCommand
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):

        def _write_csv(conflict_args):
            with open('conflicts.csv', mode='w') as conflicts:
                csv_writer = csv.writer(conflicts, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(conflict_args)

        subscribers_tuple = Subscriber.objects.values_list('email', 'gdpr_consent', 'pk')
        clients_tuple = Client.objects.values_list('email', 'phone')
        subscriber_sms_tuple = SubscriberSMS.objects.values_list('phone', 'gdpr_consent', 'pk')
        for subscriber in subscribers_tuple:
            subscriber_email = subscriber[0]
            subscriber_gdpr_consent = subscriber[1]
            phone = None
            if subscriber_email in clients_tuple:
                created = False
                index = [x[0] for x in clients_tuple].index(subscriber_email)
                phone = clients_tuple[index][1]
                try:
                    user, created = User.objects.get_or_create(email=subscriber_email,
                                                               phone=phone,
                                                               gdpr_consent=subscriber_gdpr_consent)
                except IntegrityError:
                    _write_csv([subscriber[2], subscriber_email])
                if created:
                    continue

            User.objects.get_or_create(email=subscriber_email,
                                       phone=phone,
                                       gdpr_consent=subscriber_gdpr_consent)
        for subscriber in subscriber_sms_tuple:
            subscriber_sms_phone = subscriber[0]
            subscriber_sms_gdpr_consent = subscriber[1]
            mail = None
            if subscriber_sms_phone in clients_tuple:
                created = False
                index = [x[1] for x in clients_tuple].index(subscriber_sms_phone)
                mail = clients_tuple[index][0]
                try:
                    user, created = User.objects.get_or_create(phone=subscriber_sms_phone,
                                                               email=mail,
                                                               defaults={
                                                                   'gdpr_consent': subscriber_sms_gdpr_consent
                                                                         }
                                                               )
                except IntegrityError:
                    _write_csv([subscriber[2], subscriber_sms_phone])
                if not created and user.gdpr_consent != subscriber_sms_gdpr_consent:
                    _write_csv([subscriber[2], subscriber_sms_phone])
                continue
            User.objects.get_or_create(email=mail,
                                       phone=subscriber_sms_phone,
                                       gdpr_consent=subscriber_gdpr_consent)
