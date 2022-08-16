import requests,json,os
try:
    while(1):
        escolha = input("Cliente: ").lower()
        if(escolha in ["clear","cls"]):
            os.system('cls')
            continue
        response = json.loads(requests.post("http://localhost/ChatBot",json={"Payload":escolha}).text)["Payload"]
        print(f"Bot: {response}")
        if(response=="Muito obrigado, até mais. =)"):
            break
except KeyboardInterrupt:
    pass