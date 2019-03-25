from django.contrib import admin
from .models import locations, Police, Health, Hood, Profile, Business


admin.site.register(locations)
admin.site.register(Police)
admin.site.register(Health)
admin.site.register(Hood)
admin.site.register(Profile)
admin.site.register(Business)


