from trainer import bot

def chat(usuario):
    while True:
        pergunta = input(f"{usuario}: ")
        
        if pergunta == "0":
            break
            
        response = bot.get_response(pergunta)
        print(f"Monokuma: {response}")
        

def Main():

    print("Olá! Eu sou o Monokuma!!!")
    
    usuario = input("Por favor, digite o seu nome para eu saber quem você é: ")
    
    print(f"Muito obrigado!!! Vamos iniciar nossa conversa, {usuario}.")
    
    chat(usuario)
    
 
if __name__ == "__main__":
    Main()