from django.contrib import admin
from .models import EventsModel,User
# Register your models here.

admin.site.register(EventsModel)
admin.site.register(User)