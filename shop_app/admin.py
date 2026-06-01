from django.contrib import admin


from .models import Blog,Category,Product

admin.site.register(Blog)
admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)