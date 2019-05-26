from django.contrib import admin

# Register your models here.
from .models import Category, HumanName, List


class ListAdmin(admin.ModelAdmin):
    list_display = ("state", "date", "human_name", "category", "money", "memo", "deadline")


admin.site.register(Category)
admin.site.register(HumanName)
admin.site.register(List, ListAdmin)

