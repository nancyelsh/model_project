from django.contrib import admin
from .models import Restaurant

class RstaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('open', )
    search_fields = ('name', )



# Register your models here.
admin.site.register(Restaurant, RstaurantAdmin)