from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Pet, Profile, Post


# Register your models here.
# class PetInline(admin.StackedInline):
#     model = Pet


class PetAdmin(admin.ModelAdmin):
    model = Pet


class PostAdmin(admin.ModelAdmin):
    model = Post

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Pet, PetAdmin)
