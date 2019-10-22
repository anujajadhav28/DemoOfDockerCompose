from flask import Flask, request
import json
from pymongo import MongoClient
cli=MongoClient('mongo',27017)
db=cli.mtdatabase
col=db.mycollection
app=Flask(__name__)
@app.route('/',methods=['GET','POST','PUT','DELETE'])
def task():
    if request.method=='GET':
        value=col.find()
        l=[]
        for i in value:
            l.append(i)
        return(str(l))
    elif request.method=='POST':
        value=request.get_json()
        col.insert_one(value)
        return 'Your entry has been Posted successfully!'
    elif request.method=='PUT':
        value=request.get_json()
        col.update_one(value[0],{"$set":value[1]})
        return 'put done'
    elif request.method=='DELETE':
        value=request.get_json()
        col.delete_one(value)
        return 'Entry has been deleted successfully!'
if  __name__ == "__main__":
    app.run(debug=True,port=9090,host='0.0.0.0')
