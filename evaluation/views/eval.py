from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from mdm.models import EvalPlan
from evaluation.serializers import EvalPlanSerializer
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
    print(eval_plan_no)
    eval_plan_list = EvalPlan.objects.filter(del_yn='N')
    eval_plan_list_serializer = EvalPlanSerializer(eval_plan_list, many=True)
    result.update(eval_plan_list=eval_plan_list_serializer.data)

    if eval_plan_no is not None:
        plan_qs = EvalPlan.objects.get(eval_plan_no=eval_plan_no)
    else:
        plan_qs = EvalPlan.objects.get(eval_plan_no=eval_plan_list[0].eval_plan_no)

    eval_plan_serializer = EvalPlanSerializer(plan_qs)
    result.update(eval_plan_detail=eval_plan_serializer.data)

    return render(request, 'eval/eval_main.html', result)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_evaluation(request, pk, *args, **kwargs):
    '''
    모든 평가를 완료하였을때 완료페이지 이동
    '''
    print("================")
    print("관계번호 : ", pk)
    # 1. 관계번호로 피평가자 id 평가type select

    # 2.
    print("================")
    eval_cnt = 1
    eval_type_nm = "자기역량평가"

    eval_item = [
        {
            'eval_item_id': 1,
            'eval_item': "1. 역량평가에 사용될 질문인가?",
            'eval_item_detail': [
                {
                    'detail_id': 1,
                    'detail_nm': '매우 그렇지않다'
                },
                {
                    'detail_id': 2,
                    'detail_nm': '그렇지않다'
                },
                {
                    'detail_id': 3,
                    'detail_nm': '보통이다'
                },
                {
                    'detail_id': 4,
                    'detail_nm': '그렇다'
                },
                {
                    'detail_id': 5,
                    'detail_nm': '매우 그렇다'
                },
            ]
        },
        {
            'eval_item_id': 2,
            'eval_item': "2. 역량평가에 사용될 질문인가?",
            'eval_item_detail': [
                {
                    'detail_id': 1,
                    'detail_nm': '매우 그렇지않다'
                },
                {
                    'detail_id': 2,
                    'detail_nm': '그렇지않다'
                },
                {
                    'detail_id': 3,
                    'detail_nm': '보통이다'
                },
                {
                    'detail_id': 4,
                    'detail_nm': '그렇다'
                },
                {
                    'detail_id': 5,
                    'detail_nm': '매우 그렇다'
                },
            ]
        },
        {
            'eval_item_id': 3,
            'eval_item': "3. 역량평가에 사용될 질문인가?",
            'eval_item_detail': [
                {
                    'detail_id': 1,
                    'detail_nm': '매우 그렇지않다'
                },
                {
                    'detail_id': 2,
                    'detail_nm': '그렇지않다'
                },
                {
                    'detail_id': 3,
                    'detail_nm': '보통이다'
                },
                {
                    'detail_id': 4,
                    'detail_nm': '그렇다'
                },
                {
                    'detail_id': 5,
                    'detail_nm': '매우 그렇다'
                },
            ]
        },
        {
            'eval_item_id': 4,
            'eval_item': "4. 역량평가에 사용될 질문인가?",
            'eval_item_detail': [
                {
                    'detail_id': 1,
                    'detail_nm': '매우 그렇지않다'
                },
                {
                    'detail_id': 2,
                    'detail_nm': '그렇지않다'
                },
                {
                    'detail_id': 3,
                    'detail_nm': '보통이다'
                },
                {
                    'detail_id': 4,
                    'detail_nm': '그렇다'
                },
                {
                    'detail_id': 5,
                    'detail_nm': '매우 그렇다'
                },
            ]
        },
        {
            'eval_item_id': 5,
            'eval_item': "5. 역량평가에 사용될 질문인가?",
            'eval_item_detail': [
                {
                    'detail_id': 1,
                    'detail_nm': '매우 그렇지않다'
                },
                {
                    'detail_id': 2,
                    'detail_nm': '그렇지않다'
                },
                {
                    'detail_id': 3,
                    'detail_nm': '보통이다'
                },
                {
                    'detail_id': 4,
                    'detail_nm': '그렇다'
                },
                {
                    'detail_id': 5,
                    'detail_nm': '매우 그렇다'
                },
            ]
        },
    ]

    result = dict(eval_item=eval_item, eval_rel_id=pk, eval_type_nm=eval_type_nm, **kwargs)
    if eval_cnt > 0:
        return render(request, 'eval/eval_competency_form.html', result)
    else:
        return HttpResponseRedirect(reverse('evaluation:eval_complete', kwargs={**kwargs}))


@api_view(['POST'])
@permission_classes([AllowAny])
def insert_evaluation_form(request, pk, *args, **kwargs):
    '''
    평가제출하면 제출완료 후 이후 평가 할 사항이 있으면 평가페이지로 없으면 완료페이지로 redirect
    '''
    print("======================")
    print("평가 제출")
    print("======================")
    eval_cnt = 0
    result = dict(**kwargs)
    if eval_cnt > 0:
        return HttpResponseRedirect(reverse('evaluation:eval_form', kwargs={'pk': 2, **kwargs}))
    else:
        return HttpResponseRedirect(reverse('evaluation:eval_complete', kwargs={**kwargs}))


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
    모든 평가를 완료하였을때 완료페이지 이동
    '''
    result = dict(isDiff=False, eval_rel_no=1)
    return JsonResponse(result)
