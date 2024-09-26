from django.contrib import admin
from .models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday',
        'created_at',
        'referral',
        'discount_percentage_display',
        'is_visiting'
    )
    list_editable = ('is_visiting',)
    list_filter = ('is_visiting',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
