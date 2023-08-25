import random

class Account:
  def __init__(self, user, password) -> None:
    self.user = user
    self.password = password
    self.account_number = "".join(str(random.randint(0, 9)) for _ in range(5))
    self.total_value = 0
    self.total_withdraws = 0
    self.withdraws = []
    self.MAX_WITHDRAWS = 3
    
  def deposit(self, value):
    if value <= 0:
      return "\nOperação falhou! O valor informado é inválido.\n"
    self.total_value += value
    return "\nDepósito efetuado.\n"
      
  def withdraw(self, value):
    if value <= 0:
      return "\nOperação falhou! O valor informado é inválido.\n"
    elif value > 500:
      return "\nOperação falhou! O valor informado ultrapassa o limite de saque."
    elif self.total_value < value:
      return "\nOperação falhou! Não há saldo disponível na conta.\n"
    else:
      self.total_value -= value
      self.total_withdraws += 1
      self.withdraws.append(value)
      return f"\nSaque de R$ {value:.2f} efetuado.\n"

  def view_bank_statement(self):
    return f'Saldo: R$ {self.total_value:.2f}'