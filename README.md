# Desafios do Modulo: Dominado Python para Ciência de Dados

Neste repósitorio estão minhas soluções para os desafios 1 e 2 do modulo **Dominando Python para Ciência de Dados** da DIO no Bootcamp **Potência Tech powered by iFood | Ciência de Dados**.

## Desafio - 1
[![Static Badge](https://img.shields.io/badge/sistema_bancario-v1-fff?style=for-the-badge&labelColor=137d1c)](https://github.com/alves05/Dominando-Python-para-DS/blob/main/Sistema-Bancario-v1.py)

**Objetivo Geral:** Criar um sistema bancário com as operações sacar, depositar e visualizar extrato.

**Problema de Negócio:** Um grande banco precisa modernizar seu sistema e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações depósito, saque e extrato.

**Depósito:** Só valores positivos podem ser depositados. Para primeira versão não precisará expecificar a conta no extrato.

**Saques:** O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500.00 por saque.

**Extrato:** Deve listar todos os depósitos e saques realizados. No fim da listagem deve ser exibido o
saldo atual da conta. Se o extrato estiver em branco, exibir a
mensagem "Não foram realizadas movimentações". Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

### Desafio - 2
[![Static Badge](https://img.shields.io/badge/sistema_bancario-v2-fff?style=for-the-badge&labelColor=blue)](https://github.com/alves05/Dominando-Python-para-DS/blob/main/Sistema-Bancario-v1.py)

**Objetivo Geral:** Criar duas funções novas **Cadastrar Cliente** e **Cadastrar Conta**.

**Dasafio:** Modularizar todas as tarefas em funções.

**Saque**: A função saque receberá apenas arqumentos por nome (keyword only).

**Depósito:** A função depósito receberá apenas argumentos por posição (positional only).

**Extrato:** A função extrato irá receber argumentos por posição e nome.

**Novas Funções:** Foram adicionadas 3 novas funções:
- Cadastar Cliente
- Cadastrar Conta
- Listar Contas Cadastradas (essa função será de controle do administrador do sistema do banco, terá id e senha de acesso).