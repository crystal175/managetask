from django.contrib import admin

from .models import People, Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['education', 'people_id']


admin.site.register(People)
admin.site.register(Document, DocumentAdmin)
