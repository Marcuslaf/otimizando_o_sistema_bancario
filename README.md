# Sistema Bancário em Python / Banking System in Python

## Introdução / Introduction

Este projeto é um sistema bancário simples desenvolvido em Python. Ele permite a criação de usuários e contas, realização de depósitos e saques, exibição de extratos e listagem de contas.

This project is a simple banking system developed in Python. It allows the creation of users and accounts, deposits and withdrawals, viewing account statements, and listing accounts.

## Funcionalidades / Features

- Criar usuário / Create user
- Criar conta bancária / Create bank account
- Depositar dinheiro em uma conta / Deposit money into an account
- Sacar dinheiro de uma conta / Withdraw money from an account
- Exibir extrato bancário / Display bank statement
- Listar todas as contas cadastradas / List all registered accounts

## Como Executar o Programa / How to Run the Program

1. Certifique-se de ter o Python instalado em seu computador (versão 3.6 ou superior).  
   Make sure you have Python installed on your computer (version 3.6 or later).
2. Baixe ou clone este repositório.  
   Download or clone this repository.
3. Navegue até o diretório onde o arquivo `main.py` está localizado.  
   Navigate to the directory where the `main.py` file is located.
4. Execute o seguinte comando no terminal:  
   Run the following command in the terminal:

   ```bash
   python main.py
   ```

## Uso / Usage

Ao executar o programa, um menu será exibido com as opções disponíveis:

When running the program, a menu will be displayed with the available options:

```
[1] Depositar / Deposit
[2] Sacar / Withdraw
[3] Extrato / Statement
[4] Criar Usuário / Create User
[5] Criar Conta / Create Account
[6] Listar Contas / List Accounts
[7] Sair / Exit
```

O usuário pode interagir com o sistema digitando o número correspondente à opção desejada.

The user can interact with the system by entering the number corresponding to the desired option.

## Estrutura do Código / Code Structure

O código está organizado da seguinte forma:

The code is organized as follows:

- `exibir_mensagem(titulo, mensagem)`: Exibe mensagens formatadas no terminal. / Displays formatted messages in the terminal.
- `depositar(contas, cpf, valor)`: Realiza um depósito na conta de um usuário. / Deposits money into a user's account.
- `sacar(contas, cpf, valor, limite, limite_saques)`: Realiza um saque, respeitando limites e saldo disponível. / Withdraws money while respecting limits and available balance.
- `exibir_extrato(contas, cpf)`: Mostra o extrato bancário de um usuário. / Displays a user's bank statement.
- `criar_usuario(usuarios)`: Permite a criação de um novo usuário. / Allows the creation of a new user.
- `criar_conta(usuarios, contas, agencia)`: Cria uma conta bancária vinculada a um usuário existente. / Creates a bank account linked to an existing user.
- `listar_contas(contas)`: Lista todas as contas cadastradas no sistema. / Lists all registered accounts in the system.
- `menu_principal()`: Retorna o menu principal do sistema. / Returns the main menu of the system.
- `main()`: Função principal que controla o fluxo do programa. / Main function that controls the program flow.

## Regras do Sistema / System Rules

- Cada usuário é identificado pelo CPF. / Each user is identified by their CPF.
- Um usuário pode ter apenas uma conta bancária. / A user can only have one bank account.
- Depósitos devem ser de valores positivos. / Deposits must be of positive values.
- O limite máximo de saque é de R$ 500,00 por transação. / The maximum withdrawal limit is R$ 500.00 per transaction.
- O número máximo de saques diários é 3. / The maximum number of daily withdrawals is 3.
- O extrato exibe todas as movimentações da conta e o saldo atual. / The statement displays all account transactions and the current balance.

## Autor / Author

- **Nome / Name:** Marcus Lafaiete  
- **GitHub:** [Marcuslaf](https://github.com/Marcuslaf)  
- **LinkedIn:** [marcus-lafaiete-74b084128](https://www.linkedin.com/in/marcus-lafaiete-74b084128/)  


