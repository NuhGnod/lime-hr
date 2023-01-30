INSERT INTO ablt_eval_rslt (eval_rel_no,
                            eval_sheet_no,
                            ablt_ques_no,
                            eval_trgt_clss,
                            eval_plan_no,
                            reg_mem_no,
                            modf_mem_no,
                            reg_dt,
                            modf_dt,
                            del_yn,
                            eval_stat_cd)
SELECT er.eval_rel_no,
       B.eval_sheet_no,
       B.ablt_ques_no,
       er.eval_trgt_clss,
       B.eval_plan_no,
       '{{mem_no}}',
       '{{mem_no}}',
       sysdate(),
       sysdate(),
       'N',
       'CC016001'
FROM eval_rel as er
         INNER JOIN (SELECT ep.eval_plan_no,
                            ep.eval_plan_nm,
                            es2.eval_sheet_no,
                            es2.sheet_nm,
                            es2.eval_clss,
                            es2.ablt_ques_no,
                            es2.eval_trgt_clss,
                            (SELECT cd_nm
                             FROM comm_cd
                             WHERE comm_cd = es2.eval_trgt_clss) as eval_trgt_clss_nm
                     FROM eval_plan as ep
                              INNER JOIN (SELECT es.eval_sheet_no,
                                                 es.sheet_nm,
                                                 es.eval_clss,
                                                 aeq.ablt_ques_no,
                                                 aeq.eval_trgt_clss
                                          FROM eval_sheet as es
                                                   INNER JOIN ablt_eval_ques as aeq ON es.eval_sheet_no = aeq.eval_sheet_no
                                          WHERE es.del_yn = 'N'
                                            AND aeq.del_yn = 'N') as es2
                                         ON ep.eval_sheet_no = es2.eval_sheet_no

                     WHERE ep.eval_plan_no = '{{eval_plan_no}}'
                       AND ep.del_yn = 'N') B ON er.eval_trgt_clss = B.eval_trgt_clss
WHERE er.eval_rel_no = '{{eval_rel_no}}'
  AND B.eval_trgt_clss = '{{eval_trgt_clss}}'
