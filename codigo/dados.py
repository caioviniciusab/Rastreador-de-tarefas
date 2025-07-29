import time
tarefa = {}
listataf = []


def adicionar():
    tarefa['tarefa'] = input('Nome da tarefa: ')
    tarefa['status'] = 'A fazer'
    listataf.append(tarefa.copy())
    print('\033[32mTarefa adicionada com sucesso!\033[m')
    print('-' * 30)


def atualizar():
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
    print('\033[32mTarefa atualizada com sucesso!\033[m')
    print('-' * 30)


def excluir():
    while True:
        for c in range(0, len(listataf)):
            print(f'Tarefa {c}: {listataf[c]['tarefa']} | Status: {listataf[c]['status']}')
        print('-' * 30)
        lixo = int(input('Deseja excluir qual tarefa? '))
        print(f'\033[31mA tarefa ({listataf[lixo]['tarefa']}) será excluída!\033[m')
        cert = input('Tem certeza que deseja excluir essa tarefa? [S/N] ').upper()
        if cert == 'S':
            print(f'Excluindo tarefa...')
            time.sleep(0.5)
            del listataf[lixo]
            print('\033[32mTarefa excluída com sucesso!\033[m')
            break
        else:
            exc = input('Deseja excluir alguma tarefa? [S/N] ').upper()
            if exc == 'N':
                break
            else:
                print('Escolha novamente!')
                print('-' * 30)
    print('-' * 30)


def sair():
    print('Obrigado por usar o programa!\nVolte sempre!')