import cx_Oracle
import end as end

import config

connection = None
try:
    connection = cx_Oracle.connect(
        config.username,
        config.passwd,
        config.dsn,
        encoding = config.encoding
    )
    # show the version of the Oracle Database
    print(connection.version)
    print("Connection Successful")
except cx_Oracle.Error as error:
    print(error)
    print("Connection to DB Fail")
finally:
    # release the connection
    if connection:
        connection.close()

      end close()