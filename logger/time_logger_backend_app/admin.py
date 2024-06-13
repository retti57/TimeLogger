from django.contrib import admin
from .models import MilPerson, Aircraft, Log, Notes
# Register your models here.
admin.site.register(MilPerson)
admin.site.register(Aircraft)
admin.site.register(Log)
admin.site.register(Notes)
