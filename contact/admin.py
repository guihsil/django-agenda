from django.contrib import admin
from contact.models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone', 'email', 'show',
    ordering = 'first_name',
    list_filter = 'created_date',
    search_fields = 'first_name', 'last_name', 'phone', 'email'
    list_per_page = 15
    list_max_show_all = 100
    list_display_links = 'first_name',
    list_editable = 'show',

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',