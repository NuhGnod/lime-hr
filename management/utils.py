from django.template.loader import render_to_string
from config.utils import dict_fetchall


def get_dept_choices(dept_level=1):
    sql = render_to_string('sql/euso_dept/get_euso_dept_choices.sql', {'dept_level': dept_level})
    return_list = dict_fetchall(sql)
    print("=====================")
    print("=====================")
    return tuple((dept['dept_no'], dept['dept_nm']) for dept in return_list)
