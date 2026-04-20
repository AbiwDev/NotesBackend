from django.contrib import admin
from .models import Notes, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username","password","email"]
    
    prepopulated_fields = {"username":("password","email")}


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "text", "user", "created_at", "updated_at"]
    list_filter = ["user", "created_at"]
    search_fields = ["title", "text", "user__username"]
    ordering = ["-created_at"]
