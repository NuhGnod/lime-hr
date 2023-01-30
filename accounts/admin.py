from django.contrib import admin
from accounts.models import EusoMem
from django import forms
from management.models import CommCd
admin.site.site_header = "LIME-HRM 관리"
admin.site.index_title = "LIME_HRM 관리"
admin.site.site_title = "데이터 관리"


class UserBaseForm(forms.ModelForm):
    CODE_CHOICES = (
        ('Y', 'Y'),
        ('N', 'N')
    )
    posi_cd = forms.ModelChoiceField(
        queryset=CommCd.objects.filter(del_yn='N', hi_comm_cd='CC001000'),
        label='직위',
        widget=forms.Select
    )
    duty_resp_cd = forms.ModelChoiceField(
        queryset=CommCd.objects.filter(del_yn='N', hi_comm_cd='CC002000'),
        label='직책',
        widget=forms.Select
    )
    mem_stat_cd = forms.ModelChoiceField(
        queryset=CommCd.objects.filter(del_yn='N', hi_comm_cd='CC014000'),
        label='사원상태',
        widget=forms.Select
    )
    del_yn = forms.ChoiceField(choices=CODE_CHOICES, label='삭제여부')


@admin.register(EusoMem)
class EusoMemAdmin(admin.ModelAdmin):
    list_display = [ 'username', 'name', 'del_yn', 'is_superuser']
    list_display_links = ['username']
    list_filter = ['duty_resp_cd', 'posi_cd']
    search_fields = ['name']
    form = UserBaseForm
    fieldsets = [
        ('회원정보', {'fields': ['username', 'name', 'mem_stat_cd', 'posi_cd', 'duty_resp_cd', 'del_yn', ]}),
        ("권한", {"fields": ("is_superuser", "groups")}),
    ]


# @admin.register()