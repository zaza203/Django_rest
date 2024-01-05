from django.contrib import admin
from .models import CustomUser, Book, Order, UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class OrderInline(admin.TabularInline):
    model = Order

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'profession', 'date_of_birth', 'sex', 'is_active', 'is_staff')
    search_fields = ('email', 'profession')
    inlines = [UserProfileInline, OrderInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'category', 'price')
    search_fields = ('title', 'author', 'category')
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'quantity', 'total_price', 'timestamp')
    search_fields = ('user__email', 'book__title')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'order')
    search_fields = ('user__email',)

