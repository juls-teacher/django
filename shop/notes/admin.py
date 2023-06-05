from django.contrib import admin
from notes.models import Note

# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
    )
    fields = (
        "title",
        "comment",
        "created_at",
    )
    readonly_fields = ("created_at",)
    search_fields = ("title",)
