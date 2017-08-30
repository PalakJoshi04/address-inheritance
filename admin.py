from django.contrib import admin
from .models import Customer
from .models import ContactInfo


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class ContactInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContactInfo, ContactInfoAdmin)
