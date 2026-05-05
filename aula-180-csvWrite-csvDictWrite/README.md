# 📤 Escrita de CSV com Python

Exemplo simples de como escrever um arquivo CSV em Python usando o módulo padrão csv.

---

## 🚀 O que o código faz

* Cria uma lista de clientes (dicionários)
* Gera um arquivo CSV automaticamente
* Escreve os dados linha por linha

---

## 📌 Exemplo de dados

```python
lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]
```

---

## ⚙️ Como funciona

```python
colunas = lista_clientes[0].keys()
escritor = csv.writer(f)

escritor.writerow(colunas)

for linha in lista_clientes:
    escritor.writerow(linha.values())
```

* `writerow(colunas)` → escreve o cabeçalho
* `writerow(linha.values())` → escreve os dados

---

## 📄 Saída gerada (`aula_180.csv`)

```csv
Nome,Endereço
Luiz Otávio,"Av 1, 22"
João Silva,"R. 2, ""1"""
Maria Sol,"Av B, 3A"
```

---

## 💡 Observações

* O Python trata automaticamente:

  * vírgulas dentro dos dados
  * aspas (`"`)
* Encoding utilizado:

```python
encoding='utf-8'
```

---

## ▶️ Como executar

```bash
python write_csv.py
```

---

## 📚 Requisitos

* Python 3.x

---

## 👨‍💻 Objetivo

Projeto simples para estudo de manipulação de arquivos CSV em Python.

---
