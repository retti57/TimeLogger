from django.contrib import admin
from .models import MilPerson, Aircraft, Log, Notes
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(MilPerson)
@admin.register(Aircraft)
@admin.register(Log)
@admin.register(Notes)
class CustomAdminClass(ModelAdmin):
    pass

# admin.site.register(MilPerson)
# admin.site.register(Aircraft)
# admin.site.register(Log)
# admin.site.register(Notes)
