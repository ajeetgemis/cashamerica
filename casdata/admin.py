from django.contrib import admin
from .models import registercustomer,cardnumbers
# Register your models here.

admin.site.register(registercustomer)

#admin.site.register(cardnumbers)
@admin.register(cardnumbers)
class carddetails(admin.ModelAdmin):
    list_display=['cardnumber','dateandtime']

