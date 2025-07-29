import dados
print('-' * 30)
print(f'{'RASTREADOR DE TAREFAS':^30}')
print('-' * 30)

while True:
    print('1 - Adicionar tarefa')
    print('2 - Atualizar tarefa')
    print('3 - Excluir tarefa')
    print('4 - Sair')
    print('-' * 30)
    resp = int(input('Escolha uma opção: '))
    if resp == 1:
        dados.adicionar()
    if resp == 2:
        dados.atualizar()
    if resp == 3:
        dados.excluir()
    if resp == 4:
        dados.sair()
        break