from django.contrib import admin
from . models import Product, Customer, Reservation, Feedback
# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'ProductId', 'price', 'food_name', 'food_category', 'sub_category', 'Image')

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'village', 'city', 'mobile', 'pincode', 'state')
    search_fields = ('name', 'village', 'city', 'mobile', 'pincode', 'state')

@admin.register(Reservation)
class ReservationModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'guests')
    search_fields = ('name', 'email', 'date', 'time', 'guests')
    list_filter = ('date', 'time', 'guests')

@admin.register(Feedback)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'comment']

