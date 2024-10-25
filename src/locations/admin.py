from django.contrib import admin
from .models import Location, LocationImage
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from klingon.admin import TranslationInline, create_translations
from django.contrib.sessions.models import Session

@admin.register(Location)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp','updated','tag','id','user']
    list_filter = ["updated",'timestamp']
    search_fields = ['title','tag']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [TranslationInline]
    # actions = [create_translations]
    class Meta:
        model = Location

@admin.register(LocationImage)
class PostImageModelAdmin(admin.ModelAdmin):
    list_display = ['image','location','created']
    class Meta:
        model = LocationImage

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('id',)}),
    )


# admin.site.register(User, MyUserAdmin)
