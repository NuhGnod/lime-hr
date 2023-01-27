from django.contrib import admin
from management.models import EvalItem


# Register your models here.
@admin.register(EvalItem)
class EvalItemAdmin(admin.ModelAdmin):
    list_display = ['eval_item_no', 'eval_item_clss', 'item_nm', 'del_yn', 'modf_dt']
    list_display_links = ['item_nm']
    list_filter = ['eval_item_clss']
    search_fields = ['item_nm']
    fieldsets = [
        ('평가구분', {'fields': ['eval_item_clss']}),
        ('평가항목', {'fields': ['item_nm', 'item_desc']}),
        ('등록 및 수정사원', {'fields': ['reg_mem_no', 'modf_mem_no']})
    ]
