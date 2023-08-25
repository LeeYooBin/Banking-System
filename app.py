class Balance:
    def __init__(self):
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

menu = '''
[1] - Depósito
[2] - Saque
[3] - Ver extrato
[4] - Sair
'''

if __name__ == "__main__":
  balance = Balance()

  while True:
    print(menu)
    n = int(input("Selecione uma opção: "))
    print()

    if n == 1:
      value = float(input("Insira o valor a ser depositado: "))
      print(balance.deposit(value))
    elif n == 2:
      if balance.total_withdraws == balance.MAX_WITHDRAWS:
        print("\nOperação falhou! Limite de saques diários atingido.\n")
      elif balance.total_value == 0:
        print("\nOperação falhou! Não há saldo disponível na conta.\n")
      else:
        value = float(input("Insira o valor a ser sacado: "))
        print(balance.withdraw(value))
    elif n == 3:
      print(balance.view_bank_statement())
    elif n == 4:
      print("\nPrograma encerrado!\n")
      break
    else:
      print("\nOpção inválida! Por favor, tente novamente.\n")