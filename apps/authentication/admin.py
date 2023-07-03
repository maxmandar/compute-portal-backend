from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import CustomUser, CustomGroup



# Register your CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # add any additional fields you want to display in the user admin view
    list_display = ['username', 'email', 'fullname', 'is_staff', 'groups_display']

    def groups_display(self, obj):
        """
        Returns a string containing the names of the groups the user belongs to, separated by commas.
        """
        return ", ".join([group.name for group in obj.groups.all()])
    groups_display.short_description = 'Groups'
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal Info'), {'fields': ('email', 'full_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (('Important Dates'), {'fields': ('last_login', 'date_joined')}),
        (('Groups'), {'fields': ('groups',)})
    )


# Register your CustomGroup model
@admin.register(CustomGroup)
class CustomGroupAdmin(GroupAdmin):
    # add any additional fields you want to display in the group admin view
    list_display = ['name', 'description', 'active']
    fieldsets = (
        (None, {'fields': ('name', 'description', 'active')}),
    )

