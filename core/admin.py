from django.contrib import admin
from .models import BoardSaying, EmailSending

@admin.register(BoardSaying)
class BoardSayingAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'created_at')
    search_fields = ('nickname', 'message')

@admin.register(EmailSending)
class EmailSendingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
