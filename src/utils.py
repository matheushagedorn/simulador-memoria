def exibir_estado(memoria_principal, area_swap):
    print("Memória Principal:", memoria_principal)
    print("Área de Swap:", area_swap)

def processar_novo_processo(processo, memoria_principal, area_swap, capacidade_memoria):
    if len(memoria_principal) < capacidade_memoria:
        memoria_principal.append(processo)
        print(f"Novo processo recebido: {processo}. Adicionado à memória principal.")
    else:
        processo_removido = memoria_principal.pop(0)  # FIFO
        area_swap.append(processo_removido)
        memoria_principal.append(processo)
        print(f"Novo processo recebido: {processo}. Política FIFO aplicada: {processo_removido} removido para a swap.")
    
    exibir_estado(memoria_principal, area_swap)