# 📊 Leitura de CSV com Python

Este projeto demonstra como ler arquivos CSV em Python utilizando o módulo nativo csv.

## 📁 Estrutura

```
.
├── aula_178.csv
└── aula_178_CSV.py
```

---

## 🚀 Funcionalidades

O código mostra duas formas de leitura de arquivos CSV:

### 1. 📌 `csv.reader` (lista)

Lê cada linha do CSV como uma lista:

```python
['Nome', 'Idade', 'Endereço']
['João Paulo Pedrosa Soares', '40', 'Rua da boa nova 118, seg, esq, trs']
```

---

### 2. 📌 `csv.DictReader` (dicionário)

Lê cada linha como um dicionário, usando o cabeçalho como chave:

```python
{
    'Nome': 'João Paulo Pedrosa Soares',
    'Idade': '40',
    'Endereço': 'Rua da boa nova 118, seg, esq, trs'
}
```

---

## 🧠 Conceitos importantes

### 🔹 Delimitador (`delimiter=';'`)

O arquivo CSV utiliza `;` como separador em vez de `,`.

Isso é comum em arquivos gerados pelo Microsoft Excel em sistemas com configuração regional (Portugal/Brasil).

---

### 🔹 Encoding (`latin-1`)

O arquivo foi lido com:

```python
encoding='latin-1'
```

Motivo:

* Evitar erros com caracteres especiais (ex: `ç`, `ã`, `é`)
* Arquivos CSV do Excel no Windows geralmente usam `latin-1` ou `cp1252`

---

## ⚠️ Problemas comuns

### ❌ Erro de encoding

```bash
UnicodeDecodeError
```

✅ Solução:

```python
encoding='latin-1'
```

---

### ❌ Dados não separados

```python
['Nome;Idade;Endereço']
```

✅ Solução:

```python
delimiter=';'
```

---

### ❌ Leitura incorreta (string ao invés de lista)

```python
next(f)
```

✅ Use:

```python
next(leitor)
```

---

## ▶️ Como executar

```bash
python aula_178_CSV.py
```

---

## 📚 Requisitos

* Python 3.x

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo em Python.

---
