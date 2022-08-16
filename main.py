from chatbot import ChatBot
from flask import Flask, request, jsonify
import json
app = Flask(__name__)
myChatBot = ChatBot()
myChatBot.createModel()
myChatBot.loadModel()
def hasTAG(newTag:str)->bool:
    file = open('intents.json',"r",encoding="UTF-8")
    data_file = file.read()
    file.close()
    for intent in json.loads(data_file)['intents']:
        if(intent['tag']==newTag):
            return True
    return False
@app.route('/ChatBot', methods=["POST"])
def chat():
    req = request.get_json()
    resposta, intencao = myChatBot.chatbot_response(req["Payload"])
    return jsonify({"Payload":resposta})
@app.route('/Model/Create', methods=["POST"])
def LoadModel():
    password = request.headers.get('Password')
    if(password!="admin"):
        return jsonify({"Payload":"Password wrong"})
    myChatBot.createModel()
    #myChatBot.loadModel()
    return jsonify({"Payload":"Loaded Model"})
@app.route("/Model/CreateTag",methods=["POST"])
def CreateTag():
    req = request.get_json()
    password = request.headers.get('Password')
    if(password!="admin"):
        return jsonify({"Payload":"Password wrong"})
    tag = req["tag"]
    if(hasTAG(tag)):
        return jsonify({"Payload":"Already Existing Tag"})
    file = open('intents.json',"r")
    data_file = json.loads(file.read())
    file.close()
    data_file["intents"].append({"tag":tag,"patterns":[],"responses":[]})
    file = open('intents.json',"w",encoding="UTF-8")
    file.write(json.dumps(data_file))
    file.close()
    return jsonify({"Payload":"Tag created"})
@app.route("/Model/Patterns/",methods=["POST"])
def createPatterns():
    req = request.get_json()
    password = request.headers.get('Password')
    if(password!="admin"):
        return jsonify({"Payload":"Password wrong"})
    tag,pattern = req["tag"],req["patterns"]
    if(not(hasTAG(tag))):
        return jsonify({"Payload":"Tag does not exist"})
    file = open('intents.json',"r",encoding="UTF-8")
    data_file = json.loads(file.read())
    file.close()
    for intent in json.loads(data_file)['intents']:
        if(intent['tag']==tag):
            intent["patterns"].append(pattern)
    file = open('intents.json',"w")
    file.write(json.dumps(data_file))
    file.close()
@app.route("/Model/Read/",methods=["GET"])
def readModel():
    password = request.headers.get('Password')
    if(password!="admin"):
        return jsonify({"Payload":"Password wrong"})
    file = open('intents.json',"r",encoding="UTF-8")
    data_file = json.loads(file.read())
    file.close()
    return jsonify({"Payload":data_file})
app.run(port=80)