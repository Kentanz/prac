from flask import Flask,jsonify,render_template,request
from model.Category import Category
from model.Furniture import Furniture
app=Flask(__name__)
 

#GET all users
@app.route('/category',methods=['GET'])
def getAllCategory():
    try:
        categories=Category.getAllCategory()

        output={"Categories":categories}
        return jsonify(output),200
    except Exception as err:
        print(err)
        output={"Message":"Error occurred."}
        return jsonify(output),500

#Get 1 User based on userid supplied
@app.route('/category/<int:catid>/furniture',methods=['GET'])
def getFurnitureByCat(catid):
    try:
        furnitures=Furniture.getFurnitureByCat(catid) 

        if len(furnitures)>0:
            output={"furnitures":furnitures}
            return jsonify(output),200
        else:
            output={"furnitures":""}
            return jsonify(output),404
    except Exception as err:
        print(err)
        output={"Message":"Error occurred."}
        return jsonify(output),500


if __name__ == '__main__':
    app.run(debug=True) #start the flask app with default port 5000
