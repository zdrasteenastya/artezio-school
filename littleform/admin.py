from django.contrib import admin
from .models import Junior


class BookAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')

admin.site.register(Junior, BookAdmin)