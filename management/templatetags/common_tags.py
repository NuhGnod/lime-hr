from django import template
from management.models import CommCd

register = template.Library()

@register.filter
def get_code_nm(value):
    cd_nm = ''
    if value is not None:
        cd_nm = CommCd.objects.get(pk=value).cd_nm
    return cd_nm


@register.filter
def get_dept_nm(value):
    cd_nm = ''
    if value is not None:
        cd_nm = CommCd.objects.get(pk=value).cd_nm
    return cd_nm


@register.filter
def has_groups(user, group_name):
    return user.groups.filter(name=group_name).exists()
