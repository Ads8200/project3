from django.db import models
from django import forms
from django.contrib.auth.models import User

class Menu_Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey('Category', blank=False, on_delete=models.CASCADE, related_name="menu_items")
    size = models.ForeignKey('Size', blank=True, null=True, on_delete=models.CASCADE, related_name="menu_items", default='')
    pizza_style = models.ForeignKey('Pizza_Style', blank=True, null=True, on_delete=models.CASCADE, related_name="menu_items", default='')
    price = models.FloatField('Price per item', null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        if self.size is None and self.pizza_style is None:
            return f"{self.name} {self.category.name}"
        elif self.pizza_style_id is None:
            return f"{self.size.size} {self.name} {self.category.name}"
        else:
            return f"{self.size.size} {self.pizza_style.style} {self.name} {self.category.name}"

class Size(models.Model):
    size = models.CharField(max_length=60)

    def __str__(self):
        return self.size

class Pizza_Style(models.Model):
    style = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.style} pizza"

class Category(models.Model):
    name = models.CharField(max_length=200)
    menu_heading = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Placed_Order(models.Model):
    ts = models.DateTimeField
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Placed_Orders")
    total_price = models.FloatField
    comment = models.CharField(max_length=200)

    def __str__(self):
        return f"Order from {self.user.username} at {self.ts} totalling {self.total_price}"

class In_Order(models.Model):
    placed_order = models.ForeignKey('Placed_Order', on_delete=models.CASCADE, related_name="In_Order")
    menu_item = models.ManyToManyField('Menu_Item', related_name="In_Order")
    quantity = models.IntegerField
    item_price = models.FloatField
    price = models.FloatField(null=True)

    class Meta:
        verbose_name_plural = "In_order"
