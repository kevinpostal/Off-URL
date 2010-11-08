from django.contrib import admin
from url.models import *

'''
class PageInline(admin.TabularInline):
    model = Page
    extra = 0
    fields = ('page',)
'''

class UrlAdmin(admin.ModelAdmin):
    list_display = ( 'link', 'short_link','key','creation_date')
   # inlines = [
   #     PageInline,
   # ]


admin.site.register(Offensive_List)
admin.site.register(URL, UrlAdmin,)
