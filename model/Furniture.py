from model.DatabasePool import DatabasePool

class Furniture:

    @classmethod
    def getFurnitureByCat(cls,catid):
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)
            print(catid)
            sql="select * from furniture where cat_id=%s"
            cursor.execute(sql,(catid,))
            furnitures=cursor.fetchall()
            return furnitures
        finally:
            dbConn.close()
