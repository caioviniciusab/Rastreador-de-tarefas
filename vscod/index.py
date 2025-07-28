import time
tarefa = {}
listataf = []

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
        tarefa['tarefa'] = input('Nome da tarefa: ')
        tarefa['status'] = 'A fazer'
        listataf.append(tarefa.copy())
        print('-' * 30)
    if resp == 2:
        for c in range(0, len(listataf)):
            print(f'Tarefa {c}: {listataf[c]['tarefa']} | Status: {listataf[c]['status']}')
        print('-' * 30)
        atua = int(input('Deseja atualizar qual tarefa? '))
        print('-' * 30)
        print('OPÇÕES: ')
        print('1 - Em andamento')
        print('2 - Concluída')
        st = int(input('Escolha uma opção: '))
        if st == 1:
            listataf[atua]['status'] = 'Em andamento'
        if st == 2:
            listataf[atua]['status'] = 'Concluída'
        print('Tarefa atualizada com sucesso!')
        print('-' * 30)
    if resp == 3:
        while True:
            for c in range(0, len(listataf)):
                print(f'Tarefa {c}: {listataf[c]['tarefa']} | Status: {listataf[c]['status']}')
            print('-' * 30)
            lixo = int(input('Deseja excluir qual tarefa? '))
            print(f'A tarefa ({listataf[lixo]['tarefa']}) será excluída!')
            cert = input('Tem certeza que deseja excluir essa tarefa? [S/N] ').upper()
            if cert == 'S':
                print(f'Excluindo tarefa...')
                time.sleep(0.5)
                del listataf[lixo]
                print('Tarefa excluída com sucesso!')
                break
            else:
                exc = input('Deseja excluir alguma tarefa? [S/N] ').upper()
                if exc == 'N':
                    break
                else:
                    print('Escolha novamente!')
                    print('-' * 30)
        print('-' * 30)
    if resp == 4:
        print('Obrigado por usar o programa!\nVolte sempre!')
        break
