# -*- coding: utf-8 -*-

# 导入pymysql
import pymysql

# 连接数据库
conn = pymysql.connect(
    host='192.168.166.116',
    port=23306,
    user='tulian',
    password='E@ydsaf652po',
    db='EP'
)
print("链接数据库成功")

# 获取游标
cursor = conn.cursor()

# 定义变量
id_value = '018109b72e124789ae654aca5d'
COMPANY_CODE = '1'

for i in range(549999, 550009):
    sql = f"INSERT INTO `EP`.`TEMP_ETL_IMPORT` (`CREATE_UID`, `CREATE_TIME`, `UPDATE_UID`, `UPDATE_TIME`, `DELETED`, `REMARK`, `ID`, `NAME`, `ADDRESS`, `ATTN`, `TEL`, `FAX`, `EMAIL`, `COMPANY_CODE`, `TAX_MODEL`, `TAX_UNIT`, `TAX_NUM`, `TAX_RATE`, `IS_FINAL`, `NSRSBH`, `RD_ORDER_NUMBER`, `FILLING_TEMPLATE_CODE`, `PERIOD_ID`, `PROJECT_STATUS`, `APPROVE_STATUS`, `PAYABLE`, `ACCOUNTING_AMOUNT`, `TAX_LAW_AMOUNT`, `PERIOD_START`, `PERIOD_END`, `FILE_PATH`, `DERIVE_FROM`) " \
          f"VALUES ('system', NOW(), 'system', NOW(), '0', '测试1', %s, 'tttest1', 'tttest1', 'tttest1', '15300000000', 'tttest1', 'tttest1', %s, 'tttest1', 'tttest1', '100000', '0.13', b'0', '100000', '100000', '100000', '100000', '0', '0', '100000', '100000', '100000', NOW(), NOW(), '100000', 'TT_TEST');"

    cursor.execute(sql, (id_value + str(i), COMPANY_CODE + str(i),))

conn.commit()

cursor.close()
conn.close()
