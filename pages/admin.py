from django.contrib import admin
from .models import UpcomingEvents, RecentEvents
# Register your models here.

admin.site.register(UpcomingEvents)
admin.site.register(RecentEvents)
