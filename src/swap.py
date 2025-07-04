class AreaSwap:
    def __init__(self):
        self.processos = []

    def armazenar(self, processo):
        self.processos.append(processo)

    def recuperar(self, processo):
        if processo in self.processos:
            self.processos.remove(processo)
            return processo
        return None

    def estado(self):
        return self.processos.copy()