import time
import os
tarefa = {}
listataf = []

def rastreador():
    print('-' * 30)
    print(f'{'RASTREADOR DE TAREFAS':^30}')

def inicio():
    while True:
        rastreador()
        print('-' * 30)
        print('1 - Adicionar tarefa')
        print('2 - Atualizar tarefa')
        print('3 - Excluir tarefa')
        print('4 - Visualizar tarefa')
        print('5 - Sair')
        print('-' * 30)
        while True:
            resp = input('Escolha uma opção: ')
            if resp.isnumeric():
                resp = int(resp)
                if resp > 5 or resp < 1:
                    print(f'\033[31m({resp}) não existe no menu de opções. Tente novamente.\033[m')
                elif resp == 2:
                    if len(listataf) == 0:
                        print('\033[31mVocê não tem nenhuma tarefa cadastrada. Tente novamente.\033[m')
                    else:
                        break
                elif resp == 3:
                    if len(listataf) == 0:
                        print('\033[31mVocê não tem nenhuma tarefa cadastrada. Tente novamente.\033[m')
                    else:
                        break
                elif resp == 4:
                    if len(listataf) == 0:
                        print('\033[31mVocê não tem nenhuma tarefa cadastrada. Tente novamente.\033[m')
                    else:
                        break
                else:
                    break
            else:
                print('\033[31mEscreva em forma numérica.\033[m')

            
        if resp == 1:
            adicionar()
        if resp == 2:
            atualizar()
        if resp == 3:
            excluir()
        if resp == 4:
            visualizar()
        if resp == 5:
            sair()
            break


def limpatela():
    os.system('cls' if os.name == 'nt' else 'clear')


def adicionar():
    print('-' * 30)
    tarefa['tarefa'] = input('Nome da tarefa: ')
    tarefa['status'] = 'A fazer'
    listataf.append(tarefa.copy())
    print('\033[32mTarefa adicionada com sucesso!\033[m')
    print('-' * 30)
    time.sleep(1)
    limpatela()


def atualizar():
        for c in range(0, len(listataf)):
            print(f'Tarefa {c}: {listataf[c]['tarefa']} | Status: {listataf[c]['status']}')
        print('-' * 30)
        while True:
            atua = input('Deseja atualizar qual tarefa? ')
            if atua.isnumeric():
                atua = int(atua)
                if atua > (len(listataf) - 1) or atua < 0:
                    print(f'\033[31mNão tem nenhuma tarefa com o número ({atua}) cadastrada. Tente novamente.\033[m')
                else:
                    break
            else:
                print('\033[31mEscreva em forma numérica.\033[m')

        print('-' * 30)
        print('OPÇÕES: ')
        print('1 - Em andamento')
        print('2 - Concluída')
        while True:
            st = input('Escolha uma opção: ')
            if st.isnumeric():
                st = int(st)
                if st > 2 or st < 1:
                    print(f'\033[31m({st}) não existe no menu de opções. Tente novamente.\033[m')
                else:
                    break
            else:
                print('\033[31mEscreva em forma numérica.\033[m')

        if st == 1:
            listataf[atua]['status'] = 'Em andamento'
        if st == 2:
            listataf[atua]['status'] = 'Concluída'
        print('\033[32mTarefa atualizada com sucesso!\033[m')
        print('-' * 30)
        time.sleep(1)
        limpatela()


def excluir():
    while True:
        for c in range(0, len(listataf)):
            print(f'Tarefa {c}: {listataf[c]['tarefa']} | Status: {listataf[c]['status']}')
        print('-' * 30)
        while True:
            lixo = input('Deseja excluir qual tarefa? ')
            if lixo.isnumeric():
                lixo = int(lixo)
                if lixo > (len(listataf ) -1) or lixo < 0:
                    print(f'\033[31mNão tem nenhuma tarefa com o número ({lixo}) cadastrada. Tente novamente.\033[m')
                else:
                    break
            else:
                print('\033[31mEscreva em forma numérica.\033[m')
        print(f'\033[31mA tarefa ({listataf[lixo]['tarefa']}) será excluída!\033[m')
        while True:
            cert = input('Tem certeza que deseja excluir essa tarefa? [S/N] ').upper()
            if cert.isalpha():
                cert = str(cert)
                if cert == 'S':
                    print(f'Excluindo tarefa...')
                    time.sleep(0.5)
                    del listataf[lixo]
                    print('\033[32mTarefa excluída com sucesso!\033[m')
                    print('-' * 30)
                    time.sleep(1)
                    limpatela()
                    break
                elif cert == 'N':
                    exc = input('Deseja excluir alguma tarefa? [S/N] ').upper()
                    if exc == 'N':
                        break
                    else:
                        print('\033[33mEscolha novamente!\033[m')
                        print('-' * 30)
                        break
                else:
                    print('\033[31mResponda com "S" ou "N".\033[m')
            else:
                print('\033[31mResponda com "S" ou "N".\033[m')
        if cert == 'S' or exc == 'N':
            limpatela()
            break


def visualizar():
    while True:
        print('OPÇÕES: ')
        print('1 - Visualizar todas as tarefas')
        print('2 - Visualizar todas as tarefas concluídas')
        print('3 - Visualizar todas as tarefas que não foram concluídas')
        print('4 - Visualizar todas as tarefas em andamento')
        while True:
            visu = input('Escolha: ')
            if visu.isnumeric():
                visu = int(visu)
                if visu > 4 or visu < 1:
                    print(f'\033[31m({visu}) não existe no menu de opções.\033[m')
                else:
                    break
            else:
                print('\033[31mEscreva em forma numérica.\033[m')
        if visu == 1:
            for c in range(0, len(listataf)):
                print(f'Tarefa {c}: {listataf[c]['tarefa']} | Status: {listataf[c]['status']}')
            print('-' * 30)
        if visu == 2:
            for c in range(0, len(listataf)):
                if listataf[c]['status'] == 'Concluída':
                    print(f'Tarefa {c}: {listataf[c]['tarefa']} | Status: {listataf[c]['status']}')
            print('-' * 30)
        if visu == 3:
            for c in range(0, len(listataf)):
                if listataf[c]['status'] == 'A fazer':
                    print(f'Tarefa {c}: {listataf[c]['tarefa']} | Status: {listataf[c]['status']}')
            print('-' * 30)
        if visu == 4:
            for c in range(0, len(listataf)):
                if listataf[c]['status'] == 'Em andamento':
                    print(f'Tarefa {c}: {listataf[c]['tarefa']} | Status: {listataf[c]['status']}')
        while True:
            p = input('Deseja visualizar mais alguma tarefa? [S/N] ').upper()
            if p.isalpha():
                p = str(p)
                if p == 'N':
                    print('\033[33mEncerrando visualização...\033[m')
                    time.sleep(1)
                    limpatela()
                    break
                elif p == 'S':
                    break
                else:
                    print('\033[31mResponda com "S" ou "N".\033[m')
            else:
                print('\033[31mResponda com "S" ou "N".\033[m')
        if p == 'N':
            break

def sair():
    print('\033[36mObrigado por usar o programa!\nVolte sempre! :)\033[m')