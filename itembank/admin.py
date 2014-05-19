from django.contrib import admin

from model_utils.models import StatusModel
# from model_utils import Choices

from itembank.models import Itembank, Item, Option

class ItembankAdmin(admin.ModelAdmin):
    fields = ['name', 'status']    

class OptionInline(admin.TabularInline):
    model = Option
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    list_filter = ('itembank',)
    list_display = ('stem_text', 'itembank', 'active',)
    fields = ['itembank', 'stem_text', 'active'] # 'status']
    search_fields = ['stem_text']
    inlines = [OptionInline]

admin.site.register(Itembank, ItembankAdmin)
admin.site.register(Item, ItemAdmin) 

