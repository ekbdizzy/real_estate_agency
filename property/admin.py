from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through

    raw_id_fields = ('owner', )
    extra = 1


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    list_editable = ('new_building',)
    list_filter = (
        'new_building',
        "rooms_number",
        'has_balcony',
        'active',
    )
    raw_id_fields = (
        'liked_by',
    )

    inlines = [OwnerInline, ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'author',
        'flat'
    )
    list_display = (
        'author',
        'flat'
    )


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
