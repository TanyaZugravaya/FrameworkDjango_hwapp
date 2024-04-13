from django.contrib import admin
from .models import Client, Product, Order, Category


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описание (description)'
    actions = [reset_quantity]
    """Отдельный продукт"""
    # fields = ['name', 'description', 'category', 'date_added', 'price']
    readonly_fields = ['date_added', 'price']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],

            }
        ),
        (
            'Дата добавления',
            {
                'fields': ['date_added'],
            }
        ),
    ]


admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
