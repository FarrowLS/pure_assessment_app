from django.contrib import admin

from itembank.models import Itembank, Item, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    list_filter = ('itembank',)
    list_display = ('stem_text', 'itembank', 'active',)
    fields = ['itembank', 'stem_text', 'active']
    search_fields = ['stem_text']
    inlines = [OptionInline]

admin.site.register(Itembank)
admin.site.register(Item, ItemAdmin) 

