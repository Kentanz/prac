from model.DatabasePool import DatabasePool
from config.Settings import Settings
import jwt
import datetime
import bcrypt

class User:

    @classmethod
    def getUsers(cls):
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from user"
            cursor.execute(sql)
            users=cursor.fetchall()
            return users
        finally:
            dbConn.close()
    

    @classmethod
    def getUserByUserid(cls,userid):
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from user where userid=%s"
            cursor.execute(sql,(userid,))
            users=cursor.fetchall()
            return users
        finally:
            dbConn.close()

    @classmethod
    def insertUser(cls,username,email,role,password):
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            password=password.encode() #convert string to bytes
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            print(hashed)
            sql="insert into user(username,email,role,password) values(%s,%s,%s,%s)"
            # cursor.execute(sql,(username,email,role,password))
            cursor.execute(sql,(username,email,role,hashed))
            dbConn.commit()

            count=cursor.rowcount
            print(cursor.lastrowid)

            return count
        finally:
            dbConn.close()

    @classmethod
    def updateUser(cls,userid,email,password):
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="update user set email=%s,password=%s where userid=%s"
            cursor.execute(sql,(email,password,userid))
            dbConn.commit()
            count=cursor.rowcount

            return count
        finally:
            dbConn.close()

    @classmethod
    def deleteUser(cls,userid):
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="delete from user where userid=%s"
            cursor.execute(sql,(userid,))
            dbConn.commit()
            count=cursor.rowcount

            return count
        finally:
            dbConn.close()


    @classmethod
    def loginUser(cls,email,password):
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)
            pwCheck=False

            sql="select * from user where email=%s"
            cursor.execute(sql,(email,))
            users=cursor.fetchone()
            # print( users['password'])
            password=password.encode() #convert string to bytes
            dbpassword=users['password'].encode() #convert string to bytes
            print(password)
            print(dbpassword)
            # print(bcrypt.checkpw(password, dbpassword) )
            if bcrypt.checkpw(password, dbpassword): #True means valid password 
                pwCheck=True
            else:                                           #False means wrong password supplied for that user
                pwCheck=False

            #---jwt encode to generate a token----
            if pwCheck==False:
                return "Wrong Password"
            else:
                role=users['role']
                userid=users['userid']
                username=users['username']
                jwtToken=jwt.encode({"role":role,"userid":userid,"username":username,"exp":datetime.datetime.utcnow() + datetime.timedelta(seconds=7200)},Settings.secretKey,"HS256")

                print(jwtToken)
                return jwtToken

        finally:
            dbConn.close()
    