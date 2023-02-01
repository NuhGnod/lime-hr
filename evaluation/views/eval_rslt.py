import datetime
import http

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from mdm.models import EvalPlan, AbltEvalRslt, EvalRel
from urllib.parse import quote
from evaluation.serializers import EvalPlanSerializer, AbltEvalRsltSerializer
from django.utils.http import urlencode
from django.template.loader import render_to_string
from config.utils import dict_fetchall, count_fetchall
from management.models import CommCd
from accounts.models import EusoMem
from django.db import transaction
import xlwt


@api_view(['GET'])
@permission_classes([AllowAny])
def get_evaluation_rslt(request, *args, **kwargs):
    result_resp = dict(**kwargs)
    query_params = request.GET
    eval_plan_no = query_params.get('id')
    eval_plan_list = EvalPlan.objects.filter(del_yn='N').order_by('-eval_strt_dt')

    if eval_plan_no is None:
        if len(eval_plan_list) > 0:
            return redirect(reverse('evaluation:eval_rslt') + "?" + urlencode({'id': eval_plan_list[0].eval_plan_no}))
        else:
            result_resp.update(eval_plan_list=None)
            result_resp.update(eval_plan_detail=None)
            result_resp.update(eval_rslt_list=None)
            return render(request, 'eval_rslt/eval_rslt_main.html', result_resp)
    result_resp.update(eval_plan_list=eval_plan_list)

    calc_result_dict = calc_eval_rslt(eval_plan_no)

    result_resp.update(**calc_result_dict)
    return render(request, 'eval_rslt/eval_rslt_main.html', result_resp)


def calc_eval_rslt(eval_plan_no):
    eval_rslt_result = dict()
    eval_plan_qs = EvalPlan.objects.get(pk=eval_plan_no)

    sql = render_to_string('sql/eval_rslt/get_eval_rslt.sql', {"eval_plan_no": eval_plan_no})
    result_list = dict_fetchall(sql)

    # column 평균 용 변수
    tot_cc009001_sum = 0
    tot_cc009001_cnt = 0
    tot_cc009002_sum = 0
    tot_cc009002_cnt = 0
    tot_cc009003_sum = 0
    tot_cc009003_cnt = 0
    tot_cc009004_sum = 0
    tot_cc009004_cnt = 0
    tot_rslt_sum = 0
    tot_rslt_cnt = 0

    for result in result_list:
        if result['CC009004'] is not None:
            result['CC009004'] = float(result['CC009004'])
            tot_cc009004_sum += result['CC009004']
            tot_cc009004_cnt += 1

        if result['CC009003'] is not None and result['CC009002'] is not None and result['CC009001'] is not None:
            # 부하평가 비중
            result['CC009001'] = float(result['CC009001'])
            m_point = result['CC009001'] * (eval_plan_qs.m_eval_wght / 100)
            tot_cc009001_sum += result['CC009001']
            tot_cc009001_cnt += 1
            # 상사평가 비중
            result['CC009002'] = float(result['CC009002'])
            s_point = result['CC009002'] * (eval_plan_qs.s_eval_wght / 100)
            tot_cc009002_sum += result['CC009002']
            tot_cc009002_cnt += 1
            # 동료평가 비중
            result['CC009003'] = float(result['CC009003'])
            j_point = result['CC009003'] * (eval_plan_qs.j_eval_wght / 100)
            tot_cc009003_sum += result['CC009003']
            tot_cc009003_cnt += 1

            tot_rslt = s_point + j_point + m_point
            # 비중점수의 합
            result['tot_rslt'] = tot_rslt
            tot_rslt_sum += tot_rslt
            tot_rslt_cnt += 1
        else:
            tot_sum = 0
            tot_avg_cnt = 0
            if result['CC009001'] is not None:
                result['CC009001'] = float(result['CC009001'])
                tot_sum += result['CC009001']
                tot_avg_cnt += 1

                tot_cc009001_sum += result['CC009001']
                tot_cc009001_cnt += 1

            if result['CC009002'] is not None:
                result['CC009002'] = float(result['CC009002'])
                tot_sum += result['CC009002']
                tot_avg_cnt += 1

                tot_cc009002_sum += result['CC009002']
                tot_cc009002_cnt += 1

            if result['CC009003'] is not None:
                result['CC009003'] = float(result['CC009003'])
                tot_sum += result['CC009003']
                tot_avg_cnt += 1

                tot_cc009003_sum += result['CC009003']
                tot_cc009003_cnt += 1
            tot_rslt = None
            try:
                tot_rslt = tot_sum / tot_avg_cnt
                tot_rslt_sum += tot_rslt
                tot_rslt_cnt += 1
            except ZeroDivisionError:
                pass
            result['tot_rslt'] = tot_rslt

    avg_cc009001 = None
    avg_cc009002 = None
    avg_cc009003 = None
    avg_cc009004 = None
    avg_tot_rslt = None

    # 평균 20% 미만
    fall_avg_cc009001 = None
    fall_avg_cc009002 = None
    fall_avg_cc009003 = None
    fall_avg_cc009004 = None
    fall_avg_tot_rslt = None
    try:
        avg_cc009001 = round(tot_cc009001_sum / tot_cc009001_cnt, 2)
        avg_cc009002 = round(tot_cc009002_sum / tot_cc009002_cnt, 2)
        avg_cc009003 = round(tot_cc009003_sum / tot_cc009003_cnt, 2)
        avg_cc009004 = round(tot_cc009004_sum / tot_cc009004_cnt, 2)
        avg_tot_rslt = round(tot_rslt_sum / tot_rslt_cnt, 2)

        fall_avg_cc009001 = avg_cc009001 - (avg_cc009001 * 0.2)
        fall_avg_cc009002 = avg_cc009002 - (avg_cc009002 * 0.2)
        fall_avg_cc009003 = avg_cc009003 - (avg_cc009003 * 0.2)
        fall_avg_cc009004 = avg_cc009004 - (avg_cc009004 * 0.2)
        fall_avg_tot_rslt = avg_tot_rslt - (avg_tot_rslt * 0.2)

    except ZeroDivisionError:
        pass
    eval_rslt_result.update(avg_cc009001=avg_cc009001, avg_cc009002=avg_cc009002, avg_cc009003=avg_cc009003,
                            avg_cc009004=avg_cc009004, avg_tot_rslt=avg_tot_rslt,
                            fall_avg_cc009001=fall_avg_cc009001,
                            fall_avg_cc009002=fall_avg_cc009002, fall_avg_cc009003=fall_avg_cc009003,
                            fall_avg_cc009004=fall_avg_cc009004, fall_avg_tot_rslt=fall_avg_tot_rslt
                            )

    eval_rslt_result.update(eval_rslt_list=result_list)
    eval_rslt_result.update(eval_plan_detail=eval_plan_qs)
    return eval_rslt_result


@api_view(['GET'])
@permission_classes([AllowAny])
def excel_download(request):
    eval_plan_no = request.GET.get('id')
    if eval_plan_no is None:
        return HttpResponse(request, status=status.HTTPStatus.BAD_REQUEST, )

    cal_result_dict = calc_eval_rslt(eval_plan_no)

    response = HttpResponse(content_type="application/vnd.ms-excel")

    filename = cal_result_dict['eval_plan_detail'].eval_plan_nm + "_" + str(datetime.date.today()) + '.xls'

    # 다운로드 받을 때 생성될 파일명 설정
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(quote(filename))

    # 인코딩 설정
    wb = xlwt.Workbook(encoding='utf-8')
    # 생성될 시트명 설정
    ws = wb.add_sheet('평가결과')

    # 엑셀 스타일: 첫번째 열(=title)과 나머지 열(=data) 구분 위한 설정
    title_style = xlwt.easyxf(
        'pattern: pattern solid, fore_color indigo; align: horizontal center; font: color_index white;')

    # 첫번째 열에 들어갈 컬럼명 설정
    col_names = ['부서', '직급', '이름', '자기평가', '상사평가', '동료평가', '부하평가', '총평점']

    # 엑셀에 쓸 데이터 리스트화
    rows = []
    for data in cal_result_dict['eval_rslt_list']:
        rows.append(
            [data['dept_nm'], data['posi_nm'], data['name'], data['CC009004'], data['CC009002'], data['CC009003'],
             data['CC009001'], data['tot_rslt']])

    rows.append(
        ['', '', '', cal_result_dict['avg_cc009004'], cal_result_dict['avg_cc009002'], cal_result_dict['avg_cc009003'],
         cal_result_dict['avg_cc009001'], cal_result_dict['avg_tot_rslt']])
    # 첫번째 열: 설정한 컬럼명 순서대로 스타일 적용하여 생성
    row_num = 0
    for idx, col_name in enumerate(col_names):
        ws.write(row_num, idx, col_name, title_style)

    # 두번째 이후 열: 설정한 컬럼명에 맞춘 데이터 순서대로 스타일 적용하여 생성
    for row in rows:
        row_num += 1

        for col_num, attr in enumerate(row):
            data_style = xlwt.easyxf('align: horizontal right;')
            if col_num == 3:
                if cal_result_dict['fall_avg_cc009004'] is not None and attr is not None and cal_result_dict['fall_avg_cc009004'] > attr:
                    data_style = xlwt.easyxf('pattern: pattern solid, fore_color red; align: horizontal right;')
            elif col_num == 4:
                if cal_result_dict['fall_avg_cc009002'] is not None and attr is not None and cal_result_dict['fall_avg_cc009002'] > attr:
                    data_style = xlwt.easyxf('pattern: pattern solid, fore_color red; align: horizontal right;')
            elif col_num == 5:
                if cal_result_dict['fall_avg_cc009003'] is not None and attr is not None and cal_result_dict['fall_avg_cc009003'] > attr:
                    data_style = xlwt.easyxf('pattern: pattern solid, fore_color red; align: horizontal right;')
            elif col_num == 6:
                if cal_result_dict['fall_avg_cc009001'] is not None and attr is not None and cal_result_dict['fall_avg_cc009001'] > attr:
                    data_style = xlwt.easyxf('pattern: pattern solid, fore_color red; align: horizontal right;')
            elif col_num == 7:
                if cal_result_dict['fall_avg_tot_rslt'] is not None and attr is not None and cal_result_dict['fall_avg_tot_rslt'] > attr:
                    data_style = xlwt.easyxf('pattern: pattern solid, fore_color red; align: horizontal right;')

            ws.write(row_num, col_num, attr, data_style)

    wb.save(response)

    return response
