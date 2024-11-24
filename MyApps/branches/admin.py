from django.contrib import admin
from MyApps.branches.models import Branch

# Register your models here.

class BranchAdmin(admin.ModelAdmin):
    pass


admin.site.register(Branch, BranchAdmin)