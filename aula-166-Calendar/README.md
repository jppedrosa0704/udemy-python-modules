# 📘 Aula 165 — Usando o módulo `calendar` em Python

Este diretório contém um exemplo prático de como utilizar o módulo interno `calendar` para trabalhar com calendários, dias da semana e estruturação de meses em Python.

O objetivo desta aula é demonstrar como:

- Obter informações sobre meses e anos  
- Descobrir o primeiro e o último dia de um mês  
- Identificar o dia da semana de uma data  
- Gerar calendários completos  
- Iterar sobre todos os dias reais de um mês  

---

# 🧠 Conceitos abordados

## 🔹 O módulo `calendar`
O módulo `calendar` fornece ferramentas para manipular calendários de forma simples e eficiente.  
Com ele, é possível:

- Criar calendários completos (`calendar.calendar`, `calendar.month`)
- Obter o primeiro dia da semana e o último dia do mês (`monthrange`)
- Saber o dia da semana de qualquer data (`weekday`)
- Gerar a matriz de semanas de um mês (`monthcalendar`)
- Acessar nomes dos dias da semana (`day_name`)

Por padrão, o Python considera:
- **0 = segunda-feira**
- **6 = domingo**

---

# 📂 Arquivo incluído

### **aula_165_exercicio.py**

Este script demonstra:

- Como gerar a matriz de semanas de um mês usando `calendar.monthcalendar`
- Como percorrer essa matriz ignorando os dias "0" (que representam espaços vazios)
- Como imprimir todos os dias reais do mês de abril de 2026

---


