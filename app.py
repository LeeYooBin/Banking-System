from User import User

first_menu = '''
[1] - Entrar
[2] - Realizar cadastro
[3] - Sair
'''

user_menu = '''
[1] - Criar conta
[2] - Consultar conta
[3] - Sair
'''

account_menu = '''
[1] - Depósito
[2] - Saque
[3] - Ver extrato
[4] - Sair
'''

if __name__ == "__main__":
  users = [
    User("Alice", "password1"),
    User("Bob", "password2"),
    User("Charlie", "password3")
  ]
  
  while True:
    print(first_menu)
    first_menu_option = int(input("Selecione uma opção: "))
    print()
    
    if first_menu_option == 1:
      username = input("Digite o nome de usuário: ")
      user_found = next((user for user in users if user.name == username), None)
      if not user_found:
        print("\nO usuário informado não existe!")
        continue
      password = input("Digite a senha: ")
      if not password == user_found.password:
        print("\nA senha informada estava incorreta")
        continue
      while True:
        print(user_menu) 
        user_menu_option = int(input("Selecione uma opção: "))
        print()
        
        if user_menu_option == 1:
          account_password = input("Digite uma senha de 4 dígitos: ")
          print(user_found.register_account(account_password))
        elif user_menu_option == 2:
          account_number = input("Digite o número da conta: ")
          account_found = next((account for account in user_found.accounts if account.account_number == account_number), None)
          if not account_found:
            print("\nA conta informada não existe!")
            continue
          account_password = input("Digite a senha: ")
          if not account_password == account_found.password:
            print("\nSenha incorreta")
            continue
          while True:
            print(account_menu)
            account_menu_option = int(input("Selecione uma opção: "))
            print()
            
            if account_menu_option == 1:
              value = float(input("Insira o valor a ser depositado: "))
              print(account_found.deposit(value))
            elif account_menu_option == 2:
              if account_found.total_withdraws == account_found.MAX_WITHDRAWS:
                print("\nOperação falhou! Limite de saques diários atingido.\n")
              elif account_found.total_value == 0:
                print("\nOperação falhou! Não há saldo disponível na conta.\n")
              else:
                value = float(input("Insira o valor a ser sacado: "))
                print(account_found.withdraw(value))
            elif account_menu_option == 3:
              print(account_found.view_bank_statement())
            elif account_menu_option == 4:
              break
            else:
              print("\nOpção inválida! Por favor, tente novamente.\n")      
        elif user_menu_option == 3:
          break
        else:
          print("\nOpção inválida! Por favor, tente novamente.\n")
    elif first_menu_option == 2:
      name = input("Digite o seu nome: ")
      user_password: input("Digite uma senha: ")
      users.append(User(name, user_password))
      print("\nUsuário cadastrado!\n")
    elif first_menu_option == 3:
      print("Programa encerrado!\n")
      break
    else:
      print("\nOpção inválida! Por favor, tente novamente.\n")