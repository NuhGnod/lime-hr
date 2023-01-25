from django.db import connections
from django.template.loader import render_to_string


# def set_cache_data():
#     sql = render_to_string(
#             'evaluation/templates/sql/get_all_evalutation.sql', {"comm_cd": 'CD001000'})
#
#     return_list = dict_fetchall(sql)
#
#     print("===========================")
#     print(return_list)
#     print("===========================")




def dict_fetchall(sql, using='default'):
    with connections[using].cursor() as cursor:
        cursor.execute(sql)
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]


def count_fetchall(sql, using='default'):
    with connections[using].cursor() as cursor:
        cursor.execute(sql)
        count = cursor.rowcount
        return count
