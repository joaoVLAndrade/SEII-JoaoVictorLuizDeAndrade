import socket
import threading

HEADER = 64
PORT = 5050 #Define a porta que será associada ao servidor
# SERVER = "192.168.247.1"
SERVER = socket.gethostbyname(socket.gethostname()) #Retorna o ip do computador 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECTED"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um objeto socket(descritor de arquivo) que será responsável pela comunicação do servidor. Este socket utilizara a forma de comunicação stream que provê canais de comunicação bidirecional ponto-a-ponto. Além disso, será utilizado os protocolos associados ao IPv4
server.bind(ADDR)# O socket criado é associado a um servidor e uma porta

def handle_client(conn, addr):#Função responsável pela comunicação com o cliente
    print(f"[NEW CONNECTION] {addr} connected.")# Printa o endereço do cliente
    
    connected = True
    while connected: #Enquanto a conexão estiver ativa,  o servidor irá esperar por uma mensagem. Por isso é necessário criar threads, se não outros clientes não conseguiriam se conectar
        msg_length = conn.recv(HEADER).decode(FORMAT) #Define o tamanho em bytes da mensagem a ser recebida e a sua codificação
        if msg_length:#Se houver uma mensagem, ela será processada e exibida em tela 
            msg_length = int(msg_length) 
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            
            if msg == DISCONNECT_MESSAGE:
                connected = False #Finaliza a conexão caso a mensagem de desconexão seja recebida
                
            conn.send("Msg received".encode(FORMAT))
            
    conn.close()#Finaliza a comunicação com o servidor

def start():#Função que inicia o servidor
    server.listen()#O socket criado é colocado em modo de escuta. A partir deste momento ele espera por novas conexões
    print(f"[LISTENING] Servir is listening on {SERVER}")
    while True:
        conn, addr = server.accept()#Espera uma conexão. Quando esta for recebida, um novo socket será criado e será responsável pela comunicação da mesma. Além disso é retornada a porta que o cliente está utilizando
        thread = threading.Thread(target=handle_client, args=(conn,addr))# A conexão é então passadda para um atendente por uma thread, permitindo que outras conexões sejam processadas pelo servidor durante I/O Bounds
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")#Informa a quantidade de conexões ativas no momento sem incluir a do próprio servidor 

print("[Starting] server is starting...")
start()
    


