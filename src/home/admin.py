from django.contrib import admin

# Register your models here.

from django.contrib import admin
from home.models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname')
    list_display_links = ('id', 'firstname', 'lastname')
    search_fields = ('firstname', 'lastname')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Diary)
admin.site.register(ContactInfo)
admin.site.register(Project)
admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Track)
admin.site.register(Album)
admin.site.register(MusicBand)