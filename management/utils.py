from django.template.loader import render_to_string
from config.utils import dict_fetchall

def get_dept_choices():
    sql = render_to_string('sql/euso_dept/get_euso_dept_choices.sql')
    return_list = dict_fetchall(sql)
    return tuple((dept['dept_no'], dept['dept_nm']) for dept in return_list)
