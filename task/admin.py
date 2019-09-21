from django.contrib import admin
from task.models import Subscriber, SubscriberSMS, Client, User


non_editables = ['id', 'created_at', 'updated_at']


class SubscriberAdmin(admin.ModelAdmin):
    exclude = non_editables


class SubscriberSMSAdmin(admin.ModelAdmin):
    exclude = non_editables


class ClientAdmin(admin.ModelAdmin):
    exclude = non_editables


class UserAdmin(admin.ModelAdmin):
    exclude = non_editables


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(SubscriberSMS, SubscriberSMSAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(User, UserAdmin)
