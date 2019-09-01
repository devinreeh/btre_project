from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)
    list_per_page = 25
    search_fields = ('name',)

admin.site.register(Realtor, RealtorAdmin)
