from django.contrib import admin
from pages.models import UpcomingEvents
from .models import men_100_meter, men_relay, men_Long_jump, men_javelin, men_discus, men_shot_put, men_1500_meter, men_800_meter, men_400_meter, men_200_meter
# Register your models here.
admin.site.register(men_100_meter)
admin.site.register(men_200_meter)
admin.site.register(men_400_meter)
admin.site.register(men_800_meter)
admin.site.register(men_1500_meter)
admin.site.register(men_shot_put)
admin.site.register(men_discus)
admin.site.register(men_javelin)
admin.site.register(men_Long_jump)
admin.site.register(men_relay)
