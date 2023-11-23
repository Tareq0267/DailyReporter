from django.contrib import admin
from .models import Cluster, Area, Equipment, User, VibrationalReading, DailyReport, OverallProgress, Manhour, HSE, DailyUpdate

admin.site.register(Cluster)
admin.site.register(Area)
admin.site.register(Equipment)
admin.site.register(User)
admin.site.register(VibrationalReading)
admin.site.register(DailyReport)
admin.site.register(OverallProgress)
admin.site.register(Manhour)
admin.site.register(HSE)
admin.site.register(DailyUpdate)


