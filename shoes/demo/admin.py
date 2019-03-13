from django.contrib import admin
from .models import User,Shoes

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = []

@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    exclude = []
