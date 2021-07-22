from django.contrib import admin

# Register your models here.
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
	# list_display = [field.name for field in JenisPenyakit._meta.get_fields()]
	list_display = [field.name for field in Notification._meta.get_fields()]
	search_fields = [field.name for field in Notification._meta.get_fields()]



admin.site.register(Notification, NotificationAdmin)