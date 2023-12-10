from django.contrib import admin
from .models import Features, Download


# Register your models here.

@admin.register(Features)
class Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'description', 'is_visible')
    list_editable = ('title', 'description', 'is_visible')
    list_filter = ('title', 'is_visible')


admin.site.register(Download)
