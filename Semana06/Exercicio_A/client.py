import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname()) #Retorna o ip do computador 
DISCONNECT_MESSAGE = "DISCONNECTED"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Cria um objeto socket(descritor de arquivo) que será responsável pela comunicação do servidor. Este socket utilizara a forma de comunicação stream que provê canais de comunicação bidirecional ponto-a-ponto. Além disso, será utilizado os protocolos associados ao IPv4
client.connect(ADDR) #Conecta-se ao servidor

def send(msg): #Função para enviar mensagem
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) #Uma primeira mensagem é enviada para informar o tamanho da mensagem a ser recebida
    client.send(message) # Finalmente a mensagem original é enviada
    print(client.recv(2048).decode(FORMAT)) #Uma mensagem recebida pelo cliente é printada
    
send('Hello World')
send('Hello Everyone')

send(DISCONNECT_MESSAGE)
    

