from django.contrib import admin

# Register your models here.
from .models import Menu_Item, Size, Pizza_Style, Category, Placed_Order, In_Order

admin.site.register(Menu_Item)
admin.site.register(Size)
admin.site.register(Pizza_Style)
admin.site.register(Category)
admin.site.register(Placed_Order)
admin.site.register(In_Order)