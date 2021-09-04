from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class SchoolAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'address', 'geolocation')



class RouteAdmin(ImportExportModelAdmin):
    list_display = ('id', 'school_id', 'start_time_scheduled', 'stops')


    



admin.site.register(School, SchoolAdmin)
admin.site.register(Route, RouteAdmin)
