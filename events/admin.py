from django.contrib import admin
from .models import EventsModel,User
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(EventsModel,EventAdmin)
admin.site.register(User)