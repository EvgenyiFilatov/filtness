from django.contrib import admin


from .models import Clients, Referral


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
        'created_at',
        'is_visiting'
        )
    list_editable = ('is_visiting',)
    list_filter = ('is_visiting',)  # Фильтрация по полям
    ordering = ('-created_at',)  # Сортировка по дате создания
    date_hierarchy = 'created_at'  # Поддержка иерархии даты


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'referred_client'
        )
    list_editable = ('referred_client',)
