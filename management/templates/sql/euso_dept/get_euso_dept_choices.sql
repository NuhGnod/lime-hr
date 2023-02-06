WITH RECURSIVE CTE AS (SELECT dept_no,
                              dept_cd,
                              (SELECT cd_nm
                               FROM comm_cd
                               WHERE comm_cd = dept_cd)                     AS dept_group_nm,
                              dept_nm,
                              cast(dept_no as char(100) character set utf8) AS path,
                              hi_dept_no,
                              1                                             AS LEVEL
                       FROM euso_dept
                       WHERE del_yn = 'N'
                         AND hi_dept_no is NULL
                       UNION ALL
                       SELECT P.dept_no,
                              P.dept_cd,
                              (SELECT cd_nm
                               FROM comm_cd
                               WHERE comm_cd = P.dept_cd)      AS dept_group_nm,
                              P.dept_nm,
                              concat(CTE.PATH, '>', P.dept_no) AS path,
                              P.hi_dept_no,
                              1 + LEVEL                        AS LEVEL
                       FROM euso_dept P
                                INNER JOIN CTE ON P.hi_dept_no = CTE.dept_no
                       WHERE P.del_yn = 'N')
SELECT CTE.dept_no         AS dept_no,
        concat(CTE.dept_group_nm, ' | ', IFNULL(concat((SELECT dept_nm FROM euso_dept WHERE dept_no = CTE.hi_dept_no),' > '),''),
              CTE.dept_nm) AS dept_nm
FROM CTE
WHERE
    {% if dept_level is not None %}
  CTE.LEVEL > {{dept_level}}
    {% else %}
  CTE.LEVEL > 1
    {% endif %}
    {% if dept_no is not None %}
  AND dept_no = '{{dept_no}}'
    {% endif %}
ORDER BY dept_cd, path