from flask import Flask,jsonify,render_template,request,g
from config.Settings import Settings
import functools
import jwt, re

def login_required(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        token=request.headers.get('Authorization')
        print(token)

        auth=True
        #print(token.index("Bearer"))
        if token and token.index("Bearer")==0:
            token=token.split(" ")[1]
        else:
            auth=False
        if auth:
            try:
                #decode
                payload=jwt.decode(token,Settings.secretKey,'HS256');
                g.role=payload['role']
                g.userid=payload['userid']
                print(g.role)

            except Exception as err:
                print(err)
                auth=False
        
        if auth==False:
            output={"Message":"Error JWT"}
            return jsonify(output),403

        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

def admin_required(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        #Apply your own code to do the necessary checks
        # getUserid=args[0]
        print(kwargs['userid'])
        getUserid=kwargs['userid']

        admin=True

        if g.role == "admin" or g.userid == getUserid :
            admin=True
        else:
            admin=False

        if admin==False:
            output={"Message":"Not admin or auth user"}
            return jsonify(output),403

        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

def validateNumber(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        #Apply your own code to do the necessary checks
        # getUserid=args[0]
        print(kwargs['userid'])
        getUserid=kwargs['userid']

        isNum=True
        patternNumber=re.compile('[0-9]+$')

        if patternNumber.match(str(getUserid)) :
            isNum=True
        else:
            isNum=False

        if isNum==False:
            output={"Message":"Userid need to be a integer"}
            return jsonify(output),403

        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator



    