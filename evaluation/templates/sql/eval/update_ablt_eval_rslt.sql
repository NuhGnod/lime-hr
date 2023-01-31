UPDATE ablt_eval_rslt
  SET ablt_eval_rslt = '{{ablt_eval_rslt}}',
      eval_dt = sysdate(),
      modf_mem_no='{{modf_mem_no}}',
      eval_stat_cd = '{{eval_stat_cd}}'
WHERE eval_rel_no = '{{eval_rel_no}}'
  AND eval_sheet_no = '{{eval_sheet_no}}'
  AND ablt_ques_no = '{{ablt_ques_no}}'
  AND eval_trgt_clss = '{{eval_trgt_clss}}'
  AND eval_plan_no = '{{eval_plan_no}}'