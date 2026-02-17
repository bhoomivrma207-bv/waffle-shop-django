from django.contrib import admin
from .models import WaffleVariety, WaffleReviews, Store, WaffleCertificate


# Register your models here.

class WaffleReviewsInline(admin.TabularInline):
    model = WaffleReviews
    extra = 2

class WaffleVarietyAdmin(admin.ModelAdmin):
    list_display= ('name', 'type', 'date_added')
    inlines = [WaffleReviewsInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('waffle_varieties',)


class WaffleCertificateAdmin(admin.ModelAdmin):
    list_display = ('waffle','certificate_number')
    


admin.site.register(WaffleVariety, WaffleVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(WaffleCertificate, WaffleCertificateAdmin)

