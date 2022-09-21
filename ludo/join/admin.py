from django.contrib import admin

from . models import JoinRequest

# Register your models here.
class JoinAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'game','sender','receiver','response', 'is_active']
    search_fields = ['sender', 'receiver', 'game']

admin.site.register(JoinRequest, JoinAdmin)