from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    command = input("Digite um comando (ADD <nome> <número>, UPDATE <nome> <novo_número> ou LIST): ")
    s.send(command.encode())
    response = s.recv(1024).decode()
    print(f"Resposta do servidor:\n{response}")
    if input("Deseja continuar? (s/n): ").lower() != 's':
        break

s.close()