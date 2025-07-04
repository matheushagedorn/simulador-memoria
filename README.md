# Simulador de Memória

Este projeto simula a gestão de memória em um sistema operacional, utilizando uma política de substituição FIFO (First In, First Out) para gerenciar processos na memória principal e na área de swap.

## Instalação dos Requisitos

1. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/matheushagedorn/simulador-memoria.git
   cd simulador-memoria
   ```

2. (Opcional) Crie um ambiente virtual para isolar as dependências do projeto:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências necessárias (se houver). Para este projeto, não há dependências externas além do Python padrão.

## Como Funciona o Código

- **Memória Principal**: A classe `MemoriaPrincipal` gerencia os processos que estão atualmente na memória. Ela verifica se há espaço suficiente para adicionar novos processos e aplica a política FIFO para remover processos quando a memória está cheia.

- **Área de Swap**: A classe `AreaSwap` armazena processos que foram removidos da memória principal. Ela permite recuperar esses processos quando necessário.

- **Interação com o Usuário**: O arquivo `main.py` gerencia a interação com o usuário, permitindo que ele adicione novos processos, recupere processos da área de swap e visualize o estado atual da memória e da swap.

## Como Executar

1. Navegue até o diretório do projeto e execute o programa:

   ```bash
   cd simulador-memoria/src
   python main.py
   ```

2. Siga as instruções na tela para interagir com o simulador de memória. Você poderá adicionar novos processos, recuperar processos da área de swap e visualizar o estado atual da memória.