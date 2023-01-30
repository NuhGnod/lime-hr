from django.contrib import admin
from accounts.models import EusoMem
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from management.models import CommCd

admin.site.site_header = "LIME-HRM 관리"
admin.site.index_title = "LIME_HRM 관리"
admin.site.site_title = "데이터 관리"


class UserBaseForm(forms.ModelForm):
    CODE_CHOICES = (
        ('N', 'N'),
        ('Y', 'Y'),

    )
    POSI_CHOICES = (
        ("CC001001", "주임"),
        ("CC001002", "대리"),
        ("CC001003", "과장"),
        ("CC001004", "차장"),
        ("CC001005", "부장"),
        ("CC001006", "이사"),
        ("CC001007", "상무"),
        ("CC001008", "전무"),
        ("CC001009", "사장"),
        ("CC001010", "소장"),
        ("CC001011", "연구원"),
        ("CC001012", "전임연구원"),
        ("CC001013", "선임연구원")

    )

    DUTY_RESP_CHOICES = (
        ('CC002001', '팀원'),
        ('CC002002', '팀장'),
        ('CC002003', '실장'),
        ('CC002004', '본부장'),
        ('CC002005', '사업부장'),
        ('CC002006', 'CEO'),
        ('CC002007', 'CFO'),
        ('CC002008', 'COO'),

    )
    MEM_STAT_CHOICES = (
        ('CC014001', '휴직'),
        ('CC014002', '재직'),
        ('CC014003', '퇴사'),
    )
    password = ReadOnlyPasswordHashField(label="Password")
    posi_cd = forms.ChoiceField(choices=POSI_CHOICES, label='직위코드')
    duty_resp_cd = forms.ChoiceField(choices=DUTY_RESP_CHOICES, label='직책코드')
    mem_stat_cd = forms.ChoiceField(choices=MEM_STAT_CHOICES, label='사원상태')
    del_yn = forms.ChoiceField(choices=CODE_CHOICES, label='삭제여부', )



class UserCreateForm(forms.ModelForm):
    CODE_CHOICES = (
        ('N', 'N'),
        ('Y', 'Y'),

    )
    POSI_CHOICES = (
        ("CC001001", "주임"),
        ("CC001002", "대리"),
        ("CC001003", "과장"),
        ("CC001004", "차장"),
        ("CC001005", "부장"),
        ("CC001006", "이사"),
        ("CC001007", "상무"),
        ("CC001008", "전무"),
        ("CC001009", "사장"),
        ("CC001010", "소장"),
        ("CC001011", "연구원"),
        ("CC001012", "전임연구원"),
        ("CC001013", "선임연구원")

    )

    DUTY_RESP_CHOICES = (
        ('CC002001', '팀원'),
        ('CC002002', '팀장'),
        ('CC002003', '실장'),
        ('CC002004', '본부장'),
        ('CC002005', '사업부장'),
        ('CC002006', 'CEO'),
        ('CC002007', 'CFO'),
        ('CC002008', 'COO'),

    )
    MEM_STAT_CHOICES = (
        ('CC014001', '휴직'),
        ('CC014002', '재직'),
        ('CC014003', '퇴사'),
    )
    posi_cd = forms.ChoiceField(choices=POSI_CHOICES, label='직위코드')
    duty_resp_cd = forms.ChoiceField(choices=DUTY_RESP_CHOICES, label='직책코드')
    mem_stat_cd = forms.ChoiceField(choices=MEM_STAT_CHOICES, label='사원상태')
    del_yn = forms.ChoiceField(choices=CODE_CHOICES, label='삭제여부', )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EusoMemAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'del_yn', 'is_superuser']
    list_display_links = ['username']
    list_filter = ['duty_resp_cd', 'posi_cd']
    search_fields = ['name']
    form = UserBaseForm
    add_form = UserCreateForm
    fieldsets = [
        ('회원정보', {'fields': ['username', 'password', 'name', 'mem_stat_cd', 'posi_cd', 'duty_resp_cd', 'del_yn', ]}),
        ("권한", {"fields": ("is_superuser", "groups")}),
    ]

    def save_model(self, request, obj, form, change):
        print("=======================")
        obj.email = obj.username
        obj.set_password('dbzmfflem1!')
        obj.reg_mem_no = request.user.id
        obj.modf_mem_no = request.user.id
        if obj.is_superuser == 1:
            obj.is_staff = 1

        # print(request.user)
        # print(request.user.username)
        # print(request.user.email)
        # print(request.user.set_password('dbzmfflem1!'))
        # print("=======================")
        # obj.user = request.user
        # obj.user.set_email()
        # obj.user.set_password('dbzmfflem1!')
        super().save_model(request, obj, form, change)


admin.site.register(EusoMem, EusoMemAdmin)
# @admin.register()
