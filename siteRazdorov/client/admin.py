from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone', 'date', 'page')

admin.site.register(Client, ClientAdmin)
