import cx_Oracle

import config

sql = 'select DEPT_ID, DEPT_DESCRIPTION, LOCATION, CREATED_ON ' \
      'from GARRAGE.XX_DEPARTMENT ' \
      'order by DEPT_ID'
try:
    # connect to the Oracle Database
    with cx_Oracle.connect(
            config.username,
            config.passwd,
            config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            # execute the SQL statement
            cursor.execute(sql)
            # fetch all rows
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
except cx_Oracle.Error as error:
    print(error)
