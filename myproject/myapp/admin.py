from django.contrib import admin
from .models import myapp_variety,app_review,store,app_certificate

# Register your models here.

class app_review_inline(admin.TabularInline):
    model = app_review
    extra = 1


class myapp_variety_admin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date')
    inlines = [app_review_inline]

class store_admin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('app_varieties',)

class app_certificate_admin(admin.ModelAdmin):
    list_display = ('app', 'certificate_number', 'issued_date', 'valid_until')

admin.site.register(myapp_variety,myapp_variety_admin)
admin.site.register(store,store_admin)
admin.site.register(app_certificate,app_certificate_admin)



