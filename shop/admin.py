from django.contrib import admin
from .models import Product, Order

# Register your models here.



admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"


class ProductAdmin(admin.ModelAdmin):
    def Default_category(self, request, queryset):
        queryset.update(category="default")

    list_display = ('name', 'price', "discount_price", 'category')
    search_fields = ('name', "category")
    actions = ('Default_category',)
    list_editable = ("price", "category",)



admin.site.register(Product, ProductAdmin)
admin.site.register(Order)