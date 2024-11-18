from django.contrib import admin
from .models import CustomUser, CuestomRols, UsersPassword

admin.site.register(CustomUser)
admin.site.register(CuestomRols)
admin.site.register(UsersPassword)
# Register your models here.
