SELECT
    COMM_CD AS commCd,
    COMM_CD_NM AS commCdNm,
    HIRK_COMM_CD AS hirkCommCd
 FROM COMM_CD
 WHERE COMM_CD != '{{comm_cd}}'