from django.template.loader import render_to_string
from config.utils import dict_fetchall


def set_cache_data():
    sql = render_to_string(
            'sql/get_all_evalutation.sql', {"comm_cd": 'CD001000'})

    return_list = dict_fetchall(sql)

    print("===========================")
    print(return_list)
    print("===========================")