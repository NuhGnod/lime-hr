SELECT B.eval_trgt_clss,
       B.be_eval_mem_no,
       (CASE
            WHEN B.eval_stat_cd = 'CC016003' THEN 'Y'
            ELSE 'N'
           END) AS eval_stat
FROM (SELECT A.eval_trgt_clss,
             A.be_eval_mem_no,
             aer.eval_stat_cd
      FROM (SELECT er.eval_rel_no,
                   er.eval_trgt_clss,
                   er.eval_mem_no,
                   er.be_eval_mem_no,
                   B.eval_plan_no,
                   B.eval_plan_nm,
                   B.eval_sheet_no,
                   B.sheet_nm,
                   B.eval_clss,
                   B.ablt_ques_no,
                   B.eval_trgt_clss_nm
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
            WHERE eval_mem_no = '{{mem_no}}') A
               LEFT OUTER JOIN ablt_eval_rslt aer ON A.eval_rel_no = aer.eval_rel_no
          AND A.eval_sheet_no = aer.eval_sheet_no AND A.ablt_ques_no = aer.ablt_ques_no AND
                                                     A.eval_plan_no = aer.eval_plan_no
      GROUP BY A.eval_trgt_clss, A.be_eval_mem_no
      ORDER BY A.eval_trgt_clss desc) AS B
GROUP BY B.eval_trgt_clss, B.be_eval_mem_no