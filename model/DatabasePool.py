from mysql.connector import pooling
import os

class DatabasePool:
    #class variable
    # Please change to correct db conn string
    # connection_pool = pooling.MySQLConnectionPool(
    #                            pool_name="ws_pool",
    #                            pool_size=5,
    #                            host='localhost',
    #                            database='lab',
    #                            user='root',
    #                            password='Selftest01')

    connection_pool = pooling.MySQLConnectionPool(
                               pool_name="ws_pool",
                               pool_size=1,
                               host=os.environ['Host'],
                               database=os.environ['Database'],
                               user=os.environ['Username'],
                               password=os.environ['Password'])


    @classmethod
    def getConnection(cls):
        try: 
            dbConn = cls.connection_pool.get_connection()
        except Exception as err:
            print(err)

        return dbConn
