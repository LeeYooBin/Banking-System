from Account import Account

class User:
  def __init__(self, name, user_password):
    self.name = name
    self.password = user_password
    self.accounts = []
    
  def register_account(self, account_password):
    new_account = Account(self.name, account_password)
    self.accounts.append(new_account)
    details = f'''\nConta criada com sucesso!
    
Detalhes da conta
Usuário: {new_account.user}
Senha: {new_account.password}
Número: {new_account.account_number}
\n'''
    return details

# if __name__ == "__main__":
#   user = User("Robson", "12345678910")
#   print(user.register_account("123456"))
  
  