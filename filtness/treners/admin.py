from django.contrib import admin
from .models import Treners, Specialty, ClientTrainerRelationship


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price_one_time',
        'price_four_time',
        'price_eight_time'
    )


@admin.register(Treners)
class TrenersAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday',
        'number_phone'
    )
    ordering = ('id',)


@admin.register(ClientTrainerRelationship)
class ClientTrainerRelationshipAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'trainer',
        'specialty',
        'fee',
        'start_date',
        'end_date'
    )
