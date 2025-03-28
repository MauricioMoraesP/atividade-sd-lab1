from socket import *
from constCS import *

phone_book = {}

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

 
(conn, addr) = s.accept()
 
while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    if data.startswith("ADD"):
        parts = data.split(" ")
        if len(parts) != 3:
            conn.send("Formato inválido. Use: ADD <nome> <número>".encode())
            continue
        
        name = parts[1]
        number = parts[2]
        phone_book[name] = number
        conn.send(f"Contato {name}: {number} adicionado com sucesso.".encode())

    elif data.startswith("UPDATE"):
        parts = data.split(" ")
        if len(parts) != 3:
            conn.send("Formato inválido. Use: UPDATE <nome> <novo_número>".encode())
            continue
        
        name = parts[1]
        new_number = parts[2]
        if name in phone_book:
            phone_book[name] = new_number
            conn.send(f"Contato {name} atualizado para {new_number}.".encode())
        else:
            conn.send(f"Contato {name} não encontrado.".encode())

    elif data == "LIST":
        if not phone_book:
            conn.send("A agenda telefônica está vazia.".encode())
        else:
            contacts = "\n".join([f"{name}: {number}" for name, number in phone_book.items()])
            conn.send(f"Agenda Telefônica:\n{contacts}".encode())
    else:
        conn.send("Comando inválido. Use: ADD <nome> <número>, UPDATE <nome> <novo_número> ou LIST".encode())

conn.close()
s.close()
 