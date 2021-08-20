from flask import Flask,jsonify,render_template,request

app=Flask(__name__)


#hardcode 1 user json object in the users List 
users=[
    {"userid":1,"username":"John","email":"john@gmailer.com","role":"member","password":"abc123"}
    ]
#Del User based on userid supplied
@app.route('/users/<int:userid>',methods=['PUT'])
def updOneUser(userid):
    try:
        found=False
        # userData=""
        userData=request.json
        for user in users:
            uid=user["userid"]
            if userid==uid:#match the client's userid supplied
                found=True
                # userData=user
                print(users)
                user['username']=userData['username']
                user['email']=userData['email']
                user['role']=userData['role']
                user['password']=userData['password']
                print(users)
                break        
        if found:
            output={"Delete Users":user}
            return jsonify(output),200
        else:
            output={"Not Delete Users":""}
            return jsonify(output),404
    except Exception as err:
        print(err)
        output={"Message":"Error occurred."}
        return jsonify(output),500

#Del User based on userid supplied
@app.route('/users/<int:userid>',methods=['DELETE'])
def delOneUser(userid):
    try:
        found=False
        userData=""
        for user in users:
            uid=user["userid"]
            if userid==uid:#match the client's userid supplied
                found=True
                userData=user
                # print(users)
                users.remove(user)
                # print(users)
                break        
        if found:
            output={"Delete Users":userData}
            return jsonify(output),200
        else:
            output={"Not Delete Users":""}
            return jsonify(output),404
    except Exception as err:
        print(err)
        output={"Message":"Error occurred."}
        return jsonify(output),500

#GET all users
@app.route('/users',methods=['GET'])
def getUsers():
    try:
        output={"Users":users}
        return jsonify(output),200
    except Exception as err:
        print(err)
        output={"Message":"Error occurred."}
        return jsonify(output),500

#Get 1 User based on userid supplied
@app.route('/users/<int:userid>',methods=['GET'])
def getOneUser(userid):
    try:
        found=False
        userData=""
        for user in users:
            uid=user["userid"]
            if userid==uid:#match the client's userid supplied
                found=True
                userData=user
                break        
        if found:
            output={"Users":userData}
            return jsonify(output),200
        else:
            output={"Users":""}
            return jsonify(output),404
    except Exception as err:
        print(err)
        output={"Message":"Error occurred."}
        return jsonify(output),500

#POST 1 new user - Insert
@app.route('/users',methods=['POST'])
def insertUser():
    try:

        #extract the incoming request data from user
        userData=request.json#request.form.to_dict() ->if using html forms
        print(userData)
        userid=userData['userid']
        username=userData['username']
        email=userData['email']
        role=userData['role']
        password=userData['password']

        user={"userid":userid,"username":username,"email":email,"role":role,"password":password}
        users.append(user)#insert into the list of users

        output={"userid":userid}      
        return jsonify(output),201
    except Exception as err:
        print(err)
        output={"Message":"Error occurred."}
        return jsonify(output),500



#GET all users with particular role in the querystring role
#http://localhost:5000/usersQuery?role=...
@app.route('/usersQuery',methods=['GET'])
def getUsersByRole():
    try:
        queryString=request.args
        print(queryString)
        role=queryString['role']
        found=False
        userData=[]
        for user in users:
            role0=user["role"]
            if role==role0:#match the client's role supplied
                found=True
                userData.append(user)
        if found:
            output={"Users":userData}
            return jsonify(output),200
        else:
            output={"Users":""}
            return jsonify(output),404

    except Exception as err:
        print(err)
        output={"Message":"Error occurred."}
        return jsonify(output),500

if __name__ == '__main__':
    app.run(debug=True) #start the flask app with default port 5000
