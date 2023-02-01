SELECT A.id,
       A.name,
       (SELECT ed.dept_nm
        FROM euso_mem as em
                 INNER JOIN euso_dept ed on em.dept_no = ed.dept_no
        WHERE em.id = A.id)                                                 AS 'dept_nm',
       (SELECT cc.cd_nm
        FROM euso_mem as em
                 INNER JOIN comm_cd cc on em.posi_cd = cc.comm_cd
        WHERE em.id = A.id)                                                 AS 'posi_nm',
       GROUP_CONCAT(if(A.eval_trgt_clss = 'CC009004', A.avg_rslt, NULL)) AS 'CC009004',
       GROUP_CONCAT(if(A.eval_trgt_clss = 'CC009003', A.avg_rslt, NULL)) AS 'CC009003',
       GROUP_CONCAT(if(A.eval_trgt_clss = 'CC009002', A.avg_rslt, NULL)) AS 'CC009002',
       GROUP_CONCAT(if(A.eval_trgt_clss = 'CC009001', A.avg_rslt, NULL)) AS 'CC009001'
FROM (SELECT emr.id,
             emr.name,
             emr.eval_trgt_clss,
             AVG(DISTINCT epaer.avg_rslt) AS avg_rslt
      FROM (SELECT em.id,
                   em.name,
                   er.eval_rel_no,
                   er.eval_mem_no,
                   er.eval_trgt_clss
            FROM euso_mem as em
                     INNER JOIN eval_rel er ON em.id = er.be_eval_mem_no
                AND er.del_yn = 'N'
            WHERE em.del_yn = 'N'
              AND em.mem_stat_cd != 'CC014003') AS emr
               LEFT OUTER JOIN (SELECT ep.eval_plan_no,
                                  ep.eval_sheet_no,
                                  aer.eval_trgt_clss,
                                  aer.eval_rel_no,
                                  AVG(DISTINCT aer.ablt_eval_rslt) as avg_rslt
                           FROM eval_plan as ep
                                    INNER JOIN ablt_eval_rslt aer ON ep.eval_plan_no = aer.eval_plan_no
                               AND ep.eval_sheet_no = aer.eval_sheet_no
                           WHERE ep.eval_plan_no = '{{eval_plan_no}}'
                             AND aer.eval_stat_cd = 'CC016003'
                           GROUP BY ep.eval_plan_no, ep.eval_sheet_no, aer.eval_trgt_clss, aer.eval_rel_no) as epaer
                          ON emr.eval_rel_no = epaer.eval_rel_no
      GROUP BY emr.id, emr.name, emr.eval_trgt_clss) AS A
GROUP BY A.id, A.name
ORDER BY A.name