class MemoriaPrincipal:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.processos = []

    def pode_adicionar(self, processo):
        return self.uso_atual() + processo["tamanho"] <= self.capacidade

    def adicionar_processo(self, processo):
        self.processos.append(processo)
        self.exibir_estado()
        return True

    def uso_atual(self):
        return sum(p["tamanho"] for p in self.processos)

    def substituir_processo(self):
        processo_removido = self.processos.pop(0)
        print(f"Política FIFO aplicada: {processo_removido['nome']} removido da memória principal.")
        return processo_removido

    def exibir_estado(self):
        print(f"Memória Principal: {self.estado()}")

    def estado(self):
        return [{"nome": p["nome"], "tamanho": p["tamanho"]} for p in self.processos]