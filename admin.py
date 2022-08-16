import requests,json,os
os.system("cls")
while(1):
    escolha = input("1-Listar Intents\n2-Adicionar Tag\n3-Adicionar Pergunta\n4-Adicionar Resposta\n5-Treinar Modelo\nEscolha: ")
    password = input("Password: ")
    response = ""
    if(escolha=="1"):
        response = json.loads(requests.get("http://localhost/Model/Read/",headers={"Password":password}).text)["Payload"]
        if(response!="password wrong"):
            for intent in response["intents"]:
                print(intent)
            continue
    elif(escolha=="5"):
        response = json.loads(requests.post("http://localhost/Model/Create",headers={"Password":password}).text)["Payload"]
    os.system("cls")
    print(f"Server: {response}")