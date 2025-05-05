# 🏦 Sistema Bancário em Python (Refatorado com Funções)

Este projeto é uma refatoração de um sistema bancário simples, desenvolvido com foco em modularização e boas práticas em Python. A proposta é organizar o código em funções reutilizáveis, facilitando a manutenção, a leitura e a escalabilidade.

## 🔧 Funcionalidades

- **Depósito (`depositar`)**
  - Recebe argumentos **somente posicionais**: `saldo`, `valor`, `extrato`
  - Retorna novo `saldo` e `extrato` atualizado

- **Saque (`sacar`)**
  - Recebe argumentos **somente nomeados (keyword only)**: `saldo`, `valor`, `extrato`, `limite`, `numero_saques`, `limite_saques`
  - Retorna novo `saldo` e `extrato` atualizado

- **Extrato (`exibir_extrato`)**
  - Aceita argumentos mistos:
    - Posicionais: `saldo`
    - Nomeados: `extrato`

- **Cadastro de Usuário**
  - Nome completo, CPF, data de nascimento e endereço
  - Validação para evitar duplicidade de CPF

- **Cadastro de Conta Corrente**
  - Número da conta gerado sequencialmente
  - Vinculada ao CPF do usuário cadastrado

- **Filtro por CPF**
  - Permite buscar rapidamente usuários existentes

## 🧪 Simulação

O projeto vem com três usuários fictícios e contas correntes previamente criadas para fins de teste. Todas as informações são mantidas em listas de dicionários, simulando uma base de dados simples em memória.

## 💡 Tecnologias Utilizadas

- Linguagem: **Python 3.x**
- Execução via terminal (sem bibliotecas externas)

## ▶️ Como Executar

1. Clone ou baixe o repositório
2. Abra o arquivo `sistema_bancario.py` no VS Code
3. Execute com:
   - `Ctrl+F5` ou
   - Clique em `Run Python File in Terminal` com o arquivo aberto

## 📁 Estrutura do Projeto


## 📌 Objetivo Educacional

Este projeto foi desenvolvido com fins didáticos, como parte de um exercício para praticar:

- Funções em Python
- Argumentos posicionais vs nomeados
- Estruturação de dados com listas e dicionários
- Simulação de operações bancárias
