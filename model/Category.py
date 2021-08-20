from model.DatabasePool import DatabasePool

class Category:

    @classmethod
    def getAllCategory(cls):
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from category"
            cursor.execute(sql)
            category =cursor.fetchall()
            return category 
        except Exception as err:
            print(err)            
        finally:
            dbConn.close()
    

