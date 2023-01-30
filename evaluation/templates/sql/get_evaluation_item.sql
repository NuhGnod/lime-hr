SELECT aer.eval_rel_no,
       aer.eval_sheet_no,
       aer.eval_trgt_clss,
       aer.eval_plan_no,
       aer.ablt_ques_no,
       er.eval_mem_no,
       er.be_eval_mem_no,
       (
           SELECT name
             FROM euso_mem
            WHERE euso_mem.id = er.be_eval_mem_no
       ) as be_eval_mem_nm,
       aqp.question,
       aqp.ans_type,
       aeq.otpt_order
FROM ablt_eval_rslt as aer
         INNER JOIN eval_rel as er ON aer.eval_rel_no = er.eval_rel_no
         INNER JOIN ablt_eval_ques as aeq
                    on aer.eval_sheet_no = aeq.eval_sheet_no and aer.ablt_ques_no = aeq.ablt_ques_no and
                       aer.eval_trgt_clss = aeq.eval_trgt_clss
         INNER JOIN ablt_ques_pool as aqp on aeq.ablt_ques_no = aqp.ablt_ques_no
WHERE aer.eval_rel_no = '{{eval_rel_no}}'
  AND aer.eval_sheet_no = '{{eval_sheet_no}}'
  AND aer.eval_trgt_clss = '{{eval_trgt_clss}}'
  AND aer.eval_plan_no = '{{eval_plan_no}}'
ORDER BY aeq.otpt_order