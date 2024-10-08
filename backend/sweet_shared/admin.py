from django.contrib import admin

from sweet_shared.models import SweetType
# Register your models here.

@admin.register(SweetType)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)