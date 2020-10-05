from django.contrib import admin
from .models import Slider
# Register your models here.
# admin.site.register(Slider)
@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display=['title','status']
    Search_field=['title','description']
    date_hierarchy="created_at"
    prepopulated_fields={"slug":["title"]}
    list_per_page=2

