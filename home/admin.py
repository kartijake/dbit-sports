from django.contrib import admin
from home.models import Image, Sports, Facilities, Clubs, Club_image

# Register your models here.
admin.site.register(Image)
admin.site.register(Sports)
admin.site.register(Facilities)
admin.site.register(Clubs)
admin.site.register(Club_image)
