# Sistema de Agenda Telefônica - TCP Socket

## Descrição

Este sistema implementa uma agenda telefônica distribuída usando sockets TCP, onde um servidor central armazena os contatos e vários clientes podem se conectar para gerenciar a lista de contatos.

## Funcionalidades

- **Adicionar contatos**: Permite cadastrar novos nomes e números
- **Atualizar contatos**: Altera o número de um contato existente
- **Listar contatos**: Exibe todos os contatos cadastrados na agenda

### Executando o sistema

1. **Inicie o servidor**:
   ```
   python servidor.py
   ```

2. **Conecte um ou mais clientes** (em terminais separados):
   ```
   python cliente.py
   ```

### Comandos disponíveis

| Comando | Formato | Descrição |
|---------|---------|-----------|
| ADD | `ADD <nome> <número>` | Adiciona um novo contato |
| UPDATE | `UPDATE <nome> <novo_número>` | Atualiza o número de um contato existente |
| LIST | `LIST` | Lista todos os contatos cadastrados |

## Exemplos de uso

1. Adicionar um contato:
   ```
   ADD João 11987654321
   ```

2. Atualizar um número:
   ```
   UPDATE João 11999999999
   ```

3. Listar todos os contatos:
   ```
   LIST
   ```
