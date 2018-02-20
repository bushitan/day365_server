# -*- coding: utf-8 -*-
from django.contrib import admin
from lite.models import *

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)



class FileAdmin(admin.ModelAdmin):
    pass
admin.site.register(File,FileAdmin)