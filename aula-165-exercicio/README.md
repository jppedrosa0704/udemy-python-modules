# 📘 Empréstimo — Cálculo de Datas e Parcelas (Aula 165)

Este diretório contém a solução completa do exercício sobre cálculo de parcelas e datas de vencimento de um empréstimo, utilizando `datetime` e `dateutil.relativedelta`.

O objetivo é praticar manipulação de datas, geração de parcelas mensais e formatação de valores no padrão europeu.

---

# 📂 Arquivo incluído

**aula165.py**

Este script realiza:

- Criação da data inicial do empréstimo  
- Cálculo da data final (5 anos depois)  
- Geração de todas as datas de vencimento (dia 20 de cada mês)  
- Cálculo do número total de parcelas  
- Cálculo do valor de cada parcela  
- Formatação do valor no padrão europeu (1.234,56)  
- Exibição organizada de todas as parcelas  

---

# 🧠 Conceitos abordados

## 🔹 Manipulação de datas com `datetime`
- Criação de datas específicas  
- Comparação entre datas  
- Formatação com `strftime`  

## 🔹 Uso de `relativedelta`
- Soma de meses  
- Soma de anos  
- Geração de datas recorrentes  

## 🔹 Cálculo financeiro básico
- Divisão do valor total pelo número de parcelas  
- Formatação monetária no padrão europeu  

## 🔹 Estrutura de repetição
- Loop para gerar todas as datas de vencimento  
- Contagem de parcelas  

---

# ▶️ Como executar

1. Certifique-se de ter Python 3.x instalado.  
2. Instale o módulo necessário: pip install python-dateutil

3. Execute o arquivo: python aula165.p

# 📌 O que o script exibe

- Todas as **datas de vencimento** (60 meses)  
- O **número da parcela**  
- O **valor formatado** no padrão europeu  
- Um resumo final com:  
  - Valor total do empréstimo  
  - Tempo total (anos e meses)  
  - Valor de cada parcela  

---

# 🎯 Objetivo da aula

Este exercício treina:

- Lógica de datas  
- Cálculo de parcelas  
- Uso de bibliotecas externas  
- Formatação profissional de valores  
- Construção de loops com condições baseadas em datas  

É um exemplo prático de como Python pode ser usado em sistemas financeiros, relatórios e automações.

---




