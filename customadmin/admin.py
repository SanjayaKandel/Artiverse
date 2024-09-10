from django.contrib import admin
from Artworks.models import Exhibition

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'created_at','is_current','is_upcoming')
    search_fields = ('title', 'description')
    filter_horizontal = ('artworks',)  # Allows artwork selection in the admin panel
