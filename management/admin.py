from django.contrib import admin
from management.models import EusoDept, CommCd
from django import forms
from management.utils import get_dept_choices

class EusoDeptForm(forms.ModelForm):
    CODE_CHOICES = (
        ('N', 'N'),
        ('Y', 'Y'),

    )

    DEPT_CD_CHOICES = CommCd.objects.filter(del_yn='N', hi_comm_cd='CC017000').values_list('comm_cd', 'cd_nm')
    DEPT_CHOICES = get_dept_choices(0)
    dept_cd = forms.ChoiceField(choices=DEPT_CD_CHOICES, label='부서그룹')
    hi_dept_no = forms.ChoiceField(choices=DEPT_CHOICES, label='상위부서')
    dept_nm = forms.CharField(label='부서명')

    del_yn = forms.ChoiceField(choices=CODE_CHOICES, label='삭제여부', )


class EusoDeptAdmin(admin.ModelAdmin):
    list_display = ['dept_no', 'get_dept_group', 'get_hi_dept', 'dept_nm', 'del_yn']
    list_display_links = ['dept_nm']
    search_fields = ['dept_nm']
    form = EusoDeptForm

    def get_dept_group(self, obj):
        if obj.dept_cd:
            return CommCd.objects.get(comm_cd=obj.dept_cd).cd_nm
        else:
            return '부서 그룹이 없습니다.'

    get_dept_group.short_description = '부서그룹'

    def get_hi_dept(self, obj):
        if obj.hi_dept_no:
            return EusoDept.objects.get(dept_no=obj.hi_dept_no).dept_nm
        else:
            return '상위부서가 없습니다.'

    get_hi_dept.short_description = '상위부서'


admin.site.register(EusoDept, EusoDeptAdmin)
