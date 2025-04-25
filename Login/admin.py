from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    readonly_field = ('ID')


admin.site.register(User, UserAdmin)