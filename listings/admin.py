from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publised', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'price', 'list_date')
    list_editable = ('is_publised',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')

admin.site.register(Listing, ListingAdmin)
