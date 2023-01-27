#ALGORÍTIMO DE UMA EMPRESA DE RH

lista_funcionarios = []#uma lista vazia criada pra armazenar o dicionário
id_cadastrar = 0 #variavel criada pra gerar um id para o funcionário

def cadastrar_funcionario(id_cadastrar):
    #Todos os dados digitados aqui seráo guardados na lista em um dicionário
    print('-'*25,' menu cadastrar','-'*25)
    print('O id do funcionário é {}'.format(id_cadastrar))
    nome= input('Qual o nome do funcionário? ')
    setor= input('Qual o setor do funcionário? ')
    salario = float(input('Qual o salário do funcionário? '))
    dicionario_fun={
                   'id':          id_cadastrar,
                   'Funcionário': nome,
                   'setor':       setor,
                   'salário':     salario,
                    }
    lista_funcionarios.append(dicionario_fun.copy())#appen serve pra adicionar os dados numa lista e copy é pra copiar os dados do dicionário

def consultar_funcionarios():
      print('-'*20,'Menu Consultar funcionários','-'*20)
      print('1-Consultar todos os funcionários')
      print('2-Consultar funcionários por id')
      print('3-Consultar funcionário(s) por setor')
      print('4-voltar ao menu principal')
      print('-' * 20)

      cons=input('Qual opção deseja? ')

      if cons=='1':
         for funcionarios in lista_funcionarios:#o for ira percorrer a lista onde se encontra os dados dos funcionários, ficara guardado na variável funcionários
             print('-'*20)
             for keys,values in funcionarios.items():#esse segundo for tem duas variáveis,uma pra chave,outra para o valor
                 print('{}: {}'.format(keys,values))#items serve para escolher os dados no dicionário


      elif cons == '2':
           id_fun=int(input('Digite aqui o id do funcionario '))
           for idfuncionarios in lista_funcionarios:
               print('-'*20)
               if idfuncionarios['id']==id_fun:#Se na lista idfuncionarios tiver o id selecionado os dados serão printados na tela
                  for keys,values in idfuncionarios.items():
                      print('{}: {}'.format(keys,values))



      elif cons == '3':
          setor_fun = input('Digite aqui o setor do funcionário ')
          for setorfuncionarios in lista_funcionarios:
              print('-' * 20)
              if setorfuncionarios['setor'] == setor_fun:
                   for keys, values in setorfuncionarios.items():
                       print('{}: {}'.format(keys, values))


      elif cons == '4':
            return
      else:
          print('opção inválida')
          return

def remover_funcionario():
    print('-'*25,'Menu remover funcionário','-'*25)
    cod_fun=int(input('Digite aqui o id do funcionário que pretende remover '))
    for remove_func in lista_funcionarios:
        if remove_func['id']==cod_fun:
            lista_funcionarios.remove(remove_func)
            print('funcionário removido')


while True:
 print('-' * 25, 'Menu Principal', '-' * 25)
 print('Bem-vindo a empresa de RH josué soares')
 print('1-Cadastrar Funcionário')
 print('2-Consultar funcionários')
 print('3-Remover funcionário')
 print('4-Sair')
 print('-'*20)
 slct = input('Selecione uma opção ')
#menu principal
 if slct=='1':
    id_cadastrar+=1#sempre que a opção 1 for selecionado esse calculo e efetuado e é gerado automaticamente um id para o funcionario
    cadastrar_funcionario(id_cadastrar)
    continue
 elif slct=='2':
      consultar_funcionarios()

 elif slct=='3':
      remover_funcionario()
      continue

 elif slct=='4':
      print('Encerrando programa')
      break

 else:
     print('opção inválida')
     continue








