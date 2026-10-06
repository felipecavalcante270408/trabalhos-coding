# Trabalhos Práticos - Coding

**Curso:** Análise e Desenvolvimento de Sistemas  
**Disciplina:** Coding  
**Turma:** Bloco II - 2026.2

## Integrantes
- Felipe Cavalcante
- Kaio Renan

## Trabalho Prático 01
Sistema de gerenciamento de uma escola.

Classes principais: `Escola`, `SalaDeAula`, `Professor`, `Aluno` e `Endereco`.

Relacionamentos:
- Escola e SalaDeAula: **composição**
- Escola e Professor: **associação**
- Aluno e Endereco: **agregação**

Arquivo: `trabalho_pratico_01.py`

## Trabalho Prático 02
Estudo de caso de um sistema de gerenciamento de uma locadora de veículos.

O cenário trabalha com veículos, clientes, contratos, condutores e manutenções. Há especializações de veículos (Carro, Moto e Caminhao) e de clientes (PessoaFisica e PessoaJuridica).

Na implementação parcial foi utilizado o relacionamento de **composição entre ContratoLocacao e Condutor**, pois o condutor existe associado ao contrato.

Arquivo: `trabalho_pratico_02.py`

## Como executar
Tenha o Python 3 instalado e execute:

```bash
python trabalho_pratico_01.py
```

ou

```bash
python trabalho_pratico_02.py
```
