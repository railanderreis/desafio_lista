itens = dict()
lista = list()
emails = list()
val_itens = 0
qnt_email = 0

def lista_itens():
  itens['nome'] = str(input('Nome do item: '))
  itens['quantidade'] = int(input('Quantidade: '))
  itens['valor'] = int(input('Valor: '))
  global val_itens
  val_itens += (itens['quantidade'] * itens['valor'])
  lista.append(itens)
  print('\n')

def lista_emails():  
  print('Informe um e-mail: ')
  n = str(input())
  emails.append(n)
  global qnt_email
  qnt_email = len(emails)
  print('\n')

def listar_valor_emails():
    if val_itens > 0 and qnt_email > 0:
      print('\n')
      print(f'valor total dos itens:{val_itens}')
      
      valor_total = (val_itens / qnt_email)
      print('quantidade de e-mail: ',qnt_email)
      print(f'valor total a pagar por e-mail: {valor_total:.2f}$')
      print('\n')
      for i in emails:
        print('O e-mail ',i,f'deve pagar: {valor_total:.2f}$')

      print('-------------------------')  
      print('\n') 
    else:
      print('Favor inserir valores na lista de itens e de e-mails')
      print('\n')


def main():
  op = 0
  while op != 5:
    print('Escolha uma opcao!')
    print('1 - Cadastra itens, 2 - Cadastra e-mail e 3 - Listar valor por e-mail')
    op = int(input('opcao: '))
    if op == 1:
      lista_itens()
    elif op == 2:
      lista_emails()
    elif op == 3:
      listar_valor_emails()
    elif op == 5:
      print('Finalizando...')  
    else:
      print('Opcao invalida!')  

  print('terminou')


if __name__ == '__main__':
  main()
