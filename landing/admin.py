from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "client_category",
        "country",
        "birth_date",
    )
    list_filter = ("client_category",)
    search_fields = (
        "first_name",
        "last_name",
        "country",
    )


admin.site.register(Profile, ProfileAdmin)
