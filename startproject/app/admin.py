from django.contrib import admin
from .models import project_variety,project_review,store,project_certificate

# Register your models here.

class project_review_inline(admin.TabularInline):
    model = project_review
    extra = 1


class project_variety_admin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date')
    inlines = [project_review_inline]

class store_admin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('project_varieties',)

class project_certificate_admin(admin.ModelAdmin):
    list_display = ('project', 'certificate_number', 'issued_date', 'valid_until')

admin.site.register(project_variety,project_variety_admin)
admin.site.register(store,store_admin)
admin.site.register(project_certificate,project_certificate_admin)