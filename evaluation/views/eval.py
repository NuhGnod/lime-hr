from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from mdm.models import EvalPlan, AbltEvalRslt, EvalRel
from evaluation.serializers import EvalPlanSerializer
from django.utils.http import urlencode
from django.template.loader import render_to_string
from config.utils import dict_fetchall, count_fetchall
from management.models import CommCd
from accounts.models import EusoMem


@api_view(['GET'])
@permission_classes([AllowAny])
def evaluation_main(request, *args, **kwargs):
    '''
    평가 메인 페이지
    require : 평가계획목록, 나의평가진행현황
    '''
    # query string 가져오기
    result = dict(**kwargs)
    query_params = request.GET
    eval_plan_no = query_params.get('id')
    eval_plan_list = EvalPlan.objects.filter(del_yn='N')

    # 평가계획이 선택된게 없을때 제일 첫번째 평가계획이 선택되도록 redirect
    if eval_plan_no is None and len(eval_plan_list) > 0:
        return redirect(reverse('evaluation:eval') + "?" + urlencode({'id': eval_plan_list[0].eval_plan_no}))

    # 평가계획 목록 조회
    eval_plan_list_serializer = EvalPlanSerializer(eval_plan_list, many=True)
    result.update(eval_plan_list=eval_plan_list_serializer.data)

    # 평가계획 상세정보 조회
    if eval_plan_no is not None:
        plan_qs = EvalPlan.objects.get(eval_plan_no=eval_plan_no)

        eval_plan_serializer = EvalPlanSerializer(plan_qs)

        result.update(eval_plan_detail=eval_plan_serializer.data)

        # 평가 진행상태 조회
        progress_dict = calc_eval_progress(request.user.id, eval_plan_no)

        result.update(progress_dict=progress_dict)
    else:
        result.update(eval_plan_detail=None)
    return render(request, 'eval/eval_main.html', result)


def calc_eval_progress(mem_no, eval_plan_no):
    '''
        평가 진행현황 계산 함수
    '''
    progress_list = get_eval_progress(mem_no, eval_plan_no)

    tot_sub_cnt = 0
    sub_cnt = 0
    sub_stat = 'N'
    tot_superior_cnt = 0
    superior_cnt = 0
    superior_stat = 'N'
    tot_colleague_cnt = 0
    colleague_cnt = 0
    colleague_stat = 'N'
    tot_self_cnt = 0
    self_cnt = 0
    self_stat = 'N'

    for progress_item in progress_list:
        if progress_item['eval_trgt_clss'] == 'CC009001':
            # 부하평가
            tot_sub_cnt += 1
            if progress_item['eval_stat'] == 'Y':
                sub_cnt += 1
        elif progress_item['eval_trgt_clss'] == 'CC009002':
            # 상사평가
            tot_superior_cnt += 1
            if progress_item['eval_stat'] == 'Y':
                superior_cnt += 1
        elif progress_item['eval_trgt_clss'] == 'CC009003':
            # 동료평가
            tot_colleague_cnt += 1
            if progress_item['eval_stat'] == 'Y':
                colleague_cnt += 1
        elif progress_item['eval_trgt_clss'] == 'CC009004':
            # 본인평가
            tot_self_cnt += 1
            if progress_item['eval_stat'] == 'Y':
                self_cnt += 1

    if tot_sub_cnt == sub_cnt:
        if tot_sub_cnt != 0:
            sub_stat = 'Y'
        else:
            sub_stat = None

    if tot_superior_cnt == superior_cnt:
        if tot_sub_cnt != 0:
            superior_stat = 'Y'
        else:
            superior_stat = None
    if tot_colleague_cnt == colleague_cnt:
        if tot_sub_cnt != 0:
            colleague_stat = 'Y'
        else:
            colleague_stat = None
    if tot_self_cnt == self_cnt:
        if tot_sub_cnt != 0:
            self_stat = 'Y'
        else:
            self_stat = None

    return dict(CC009001=dict(tot_cnt=tot_sub_cnt, comp_cnt=sub_cnt, eval_stat=sub_stat),
                CC009002=dict(tot_cnt=tot_superior_cnt, comp_cnt=superior_cnt, eval_stat=superior_stat),
                CC009003=dict(tot_cnt=tot_colleague_cnt, comp_cnt=colleague_cnt, eval_stat=colleague_stat),
                CC009004=dict(tot_cnt=tot_self_cnt, comp_cnt=self_cnt, eval_stat=self_stat)
                )


def get_eval_progress(mem_no, eval_plan_no):
    sql = render_to_string('sql/get_my_evaluation_progress.sql', {"mem_no": mem_no, "eval_plan_no": eval_plan_no})
    return dict_fetchall(sql)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_evaluation(request, pk, *args, **kwargs):
    '''
    모든 평가정보를 select
    '''
    eval_plan_no = pk
    sql = render_to_string('sql/get_evaluation.sql',
                           {"mem_no": request.user.id, "eval_plan_no": eval_plan_no})
    eval_list = dict_fetchall(sql)
    if len(eval_list) <= 0:
        return HttpResponseRedirect(reverse('evaluation:eval_complete', kwargs={**kwargs}))

    # 평가대상
    eval_target = eval_list[0]
    eval_rel_no = eval_target['eval_rel_no']
    be_eval_mem_nm = EusoMem.objects.get(id=EvalRel.objects.get(eval_rel_no=eval_rel_no).be_eval_mem_no).name

    eval_trgt_clss = eval_target['eval_trgt_clss']
    eval_trgt_clss_nm = '자기평가'
    if eval_trgt_clss == 'CC009001':
        eval_trgt_clss_nm = '부하평가'
    elif eval_trgt_clss == 'CC009002':
        eval_trgt_clss_nm = '상사평가'
    elif eval_trgt_clss == 'CC009003':
        eval_trgt_clss_nm = '동료평가'
    eval_sheet_no = eval_target['eval_sheet_no']
    eval_qs = AbltEvalRslt.objects.filter(eval_rel_no=eval_rel_no,
                                          eval_trgt_clss=eval_trgt_clss,
                                          eval_sheet_no=eval_sheet_no,
                                          eval_plan_no=eval_plan_no)

    # 평가항목 결과가 저장되어있지않으면 insert
    if len(eval_qs) <= 0:
        insert_sql = render_to_string('sql/insert_ablt_eval_reslt.sql',
                                      {"mem_no": request.user.id, "eval_rel_no": eval_rel_no,
                                       "eval_trgt_clss": eval_trgt_clss, "eval_plan_no": eval_plan_no})
        insert_cnt = count_fetchall(insert_sql)
        print("-----------------------------------")
        print("insert : ", insert_cnt)
        print("-----------------------------------")
    eval_item_sql = render_to_string('sql/get_evaluation_item.sql',
                                     {"eval_rel_no": eval_rel_no, "eval_plan_no": eval_plan_no,
                                      "eval_trgt_clss": eval_trgt_clss, "eval_sheet_no": eval_sheet_no})
    eval_item = dict_fetchall(eval_item_sql)

    # 1 미흡, 2~4 보통, 5~7 우수, 8~10 탁월
    print("-----------------------------------")
    print("eval_item : ", eval_item)
    print("-----------------------------------")

    result = dict(eval_sheet_no=eval_sheet_no, eval_trgt_clss=eval_trgt_clss, eval_rel_no=eval_rel_no,
                  eval_plan_no=eval_plan_no, eval_item=eval_item, eval_trgt_clss_nm=eval_trgt_clss_nm,
                  be_eval_mem_nm=be_eval_mem_nm, **kwargs)

    return render(request, 'eval/eval_competency_form.html', result)


@api_view(['POST'])
@permission_classes([AllowAny])
def insert_evaluation_form(request, pk, *args, **kwargs):
    '''
    평가제출하면 제출완료 후 이후 평가 할 사항이 있으면 평가페이지로 없으면 완료페이지로 redirect
    '''

    req_data = request.data.copy()
    for key in req_data.keys():
        if key.startswith("ques_no"):
            # 항목하나씩 저장시켜준다.
            print(req_data[key])




    eval_cnt = 0
    result = dict(**kwargs)
    # if eval_cnt > 0:
    #     return HttpResponseRedirect(reverse('evaluation:eval_form', kwargs={'pk': 2, **kwargs}))
    # else:
    #     return HttpResponseRedirect(reverse('evaluation:eval_complete', kwargs={**kwargs}))


@api_view(['GET'])
@permission_classes([AllowAny])
def complete_evaluation(request, *args, **kwargs):
    '''
    모든 평가를 완료하였을때 완료페이지 이동
    '''
    return render(request, 'eval/eval_complete_message.html')


@api_view(['GET'])
@permission_classes([AllowAny])
def ajax_eval_check(request):
    '''
    평가 진행사항 확인
    '''

    result = dict(isDiff=False, eval_rel_no=1)
    return JsonResponse(result)
