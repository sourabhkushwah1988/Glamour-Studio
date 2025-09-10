from django.contrib import admin
from .models import User, Makeup, Service, Booking, Inquiry, Feedback

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'date_joined')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('date_joined', 'is_active')

@admin.register(Makeup)
class MakeupAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'is_special_deal', 'is_award_winner', 'created_at')
    search_fields = ('name', 'type', 'description')
    list_filter = ('type', 'is_special_deal', 'is_award_winner', 'created_at')
    list_editable = ('price', 'is_special_deal', 'is_award_winner')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)
    list_editable = ('price', 'is_active')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'makeup', 'event_date', 'status', 'total_price', 'created_at')
    search_fields = ('user__username', 'makeup__name', 'location')
    list_filter = ('status', 'event_date', 'created_at')
    list_editable = ('status',)

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'status', 'created_at')
    search_fields = ('name', 'email', 'phone_number', 'message')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('rating', 'created_at')
