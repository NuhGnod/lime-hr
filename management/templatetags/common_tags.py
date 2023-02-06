from django import template
from management.models import CommCd
from django.template.loader import render_to_string
from config.utils import dict_fetchall

register = template.Library()

@register.filter
def get_code_nm(value):
    cd_nm = ''
    if value is not None:
        cd_nm = CommCd.objects.get(pk=value).cd_nm
    return cd_nm


@register.filter
def get_dept_nm(value):
    dept_nm = ''
    if value is not None:
        sql = render_to_string('sql/euso_dept/get_euso_dept_choices.sql', {'dept_no': value})
        return_list = dict_fetchall(sql)

        if len(return_list) > 0:
            dept_nm = return_list[0]['dept_nm']
    return dept_nm


@register.filter
def has_groups(user, group_name):
    return user.groups.filter(name=group_name).exists()
