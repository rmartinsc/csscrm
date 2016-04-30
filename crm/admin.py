from django.contrib import admin
from .models import Address, Company, Contact, Call

# Register your models here.
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Call)
admin.site.register(Address)