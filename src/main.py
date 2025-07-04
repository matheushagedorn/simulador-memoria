from memoria import MemoriaPrincipal
from swap import AreaSwap

def mostrar_estado(memoria, swap):
    nomes_memoria = [p["nome"] for p in memoria.processos]
    nomes_swap = [p["nome"] for p in swap.processos]
    print(f"Memória Principal: {nomes_memoria} Área de Swap: {nomes_swap}")

def main():
    capacidade_memoria = int(input("Digite a capacidade da memória principal (em MB): "))
    memoria = MemoriaPrincipal(capacidade_memoria)
    swap = AreaSwap()

    while True:
        mostrar_estado(memoria, swap)
        print("Opções: [1] Adicionar novo processo  [2] Recuperar processo da swap  [3] Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '3':
            break
        elif opcao == '1':
            nome = input("Digite o nome do processo a ser carregado: ")
            tamanho = int(input(f"Digite o tamanho do processo '{nome}' (em MB): "))
            processo = {"nome": nome, "tamanho": tamanho}
            print(f"Novo processo recebido: {nome}")
            while not memoria.pode_adicionar(processo) and len(memoria.processos) > 0:
                processo_removido = memoria.substituir_processo()
                swap.armazenar(processo_removido)
                print(f"Política FIFO aplicada: {processo_removido['nome']} removido para a swap.")
            if memoria.pode_adicionar(processo):
                memoria.adicionar_processo(processo)
            else:
                print(f"Erro: o processo '{nome}' ({tamanho} MB) é maior que a capacidade total da memória principal ({memoria.capacidade} MB).")
            mostrar_estado(memoria, swap)
        elif opcao == '2':
            if not swap.processos:
                print("A área de swap está vazia.")
                continue
            nomes_swap = [p["nome"] for p in swap.processos]
            print(f"Processos na swap: {nomes_swap}")
            nome_recuperar = input("Digite o nome do processo a recuperar da swap: ")
            processo = next((p for p in swap.processos if p["nome"] == nome_recuperar), None)
            if not processo:
                print(f"O processo '{nome_recuperar}' não está na swap.")
                continue
            if memoria.pode_adicionar(processo):
                swap.recuperar(processo)
                memoria.adicionar_processo(processo)
                print(f"Processo '{nome_recuperar}' recuperado da swap e adicionado à memória principal.")
            else:
                if len(memoria.processos) == 0:
                    print(f"Erro: o processo '{nome_recuperar}' é maior que a capacidade total da memória principal ({memoria.capacidade} MB).")
                    continue
                processo_removido = memoria.substituir_processo()
                swap.armazenar(processo_removido)
                print(f"Política FIFO aplicada: {processo_removido['nome']} removido para a swap.")
                swap.recuperar(processo)
                memoria.adicionar_processo(processo)
                print(f"Processo '{nome_recuperar}' recuperado da swap e adicionado à memória principal.")
            mostrar_estado(memoria, swap)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()