UPDATE ablt_eval_ques
  SET
      modf_dt = sysdate(),
      modf_mem_no='{{modf_mem_no}}',
      del_yn = '{{del_yn}}'
WHERE eval_sheet_no = '{{eval_sheet_no}}'
  AND ablt_ques_no = '{{ablt_ques_no}}'
  AND eval_trgt_clss = '{{eval_trgt_clss}}'
