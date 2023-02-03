from django.contrib import admin
from django import forms
from mdm.models import EvalItem


class EvalItemCreateForm(forms.ModelForm):
    ITEM_CLSS_CHOICES = (
        ('CC013001', '능력'),
        ('CC013002', '태도'),
    )

    DEL_CHOISES = (
        ('N', 'N'),
        ('Y', 'Y'),
    )

    eval_item_clss = forms.ChoiceField(choices=ITEM_CLSS_CHOICES, label='평가항목분류코드')
    del_yn = forms.ChoiceField(choices=DEL_CHOISES, label='삭제여부')


class EvalItemAdmin(admin.ModelAdmin):
    list_display = ['eval_item_no', 'eval_item_clss', 'item_nm', 'del_yn', 'modf_dt']
    list_display_links = ['item_nm']
    list_filter = ['eval_item_clss']
    search_fields = ['item_nm']
    form = EvalItemCreateForm
    fieldsets = [
        ('평가항목분류코드', {'fields': ['eval_item_clss']}),
        ('평가항목', {'fields': ['item_nm', 'item_desc']}),
        ('삭제여부', {'fields': ['del_yn']})
    ]

    def save_model(self, request, obj, form, change):
        obj.reg_mem_no = request.user.id
        obj.modf_mem_no = request.user.id
        super().save_model(request, obj, form, change)


admin.site.register(EvalItem, EvalItemAdmin)