# 🔐 Geração de Números Aleatórios Seguros com `secrets` em Python

Este projeto demonstra o uso do módulo `secrets` da linguagem Python para gerar números aleatórios **seguros**, ideais para senhas, tokens e uso criptográfico.

---

## ⚠️ Diferença entre `random` e `secrets`

* `random` → gera números **pseudoaleatórios** (não seguro)
* `secrets` → gera números **criptograficamente seguros**

👉 Use `secrets` sempre que precisar de segurança.

---

## 📦 Módulos utilizados

```python
import secrets
import string as s
from secrets import SystemRandom as Sr
```

---

## 🔑 Geração de senha segura

```python
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))
```

* Gera uma senha aleatória com:

  * Letras maiúsculas e minúsculas
  * Números
  * Caracteres especiais
* Comprimento: 12 caracteres

---

## 🔐 Gerador seguro com `SystemRandom`

```python
random = secrets.SystemRandom()
```

* Usa uma fonte de aleatoriedade do sistema operacional
* Adequado para criptografia

---

## 🔢 Geração de números seguros

### ▶️ `randbelow()`

```python
secrets.randbelow(100)
```

* Retorna um número inteiro entre `0` e `99`

---

### ▶️ `choice()`

```python
secrets.choice([10, 11, 12])
```

* Retorna um elemento aleatório de uma lista

---

## ⚠️ Sobre `seed()`

```python
# random.seed(0)
```

* Não tem efeito ao usar `secrets`
* O objetivo é justamente evitar previsibilidade

---

## 🔁 Métodos disponíveis via `SystemRandom`

Mesmo usando `secrets`, você pode usar métodos semelhantes ao `random`:

---

### ▶️ `randrange(início, fim, passo)`

```python
r_range = random.randrange(10, 20, 2)
```

* Inteiro dentro de um intervalo com passo

---

### ▶️ `randint(início, fim)`

```python
r_int = random.randint(10, 30)
```

* Inteiro entre início e fim (inclusive)

---

### ▶️ `uniform(início, fim)`

```python
r_uniform = random.uniform(10, 20)
```

* Número decimal dentro do intervalo

---

## 🔀 Manipulação de listas

```python
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
```

---

### ▶️ `sample(iterável, k=N)`

```python
novos_nomes = random.sample(nomes, k=3)
```

* Seleção sem repetição
* Retorna nova lista

---

### ▶️ `choices(iterável, k=N)`

```python
novos_nomes = random.choices(nomes, k=3)
```

* Seleção com repetição

---

### ▶️ `choice(iterável)`

```python
random.choice(nomes)
```

* Retorna um único elemento

---

## 📌 Resumo

| Função       | Descrição                         |
| ------------ | --------------------------------- |
| SystemRandom | Gerador seguro baseado no sistema |
| randbelow    | Inteiro abaixo de um limite       |
| choice       | Escolhe um elemento               |
| randrange    | Inteiro com passo                 |
| randint      | Inteiro (intervalo fechado)       |
| uniform      | Número decimal                    |
| sample       | Sem repetição                     |
| choices      | Com repetição                     |

---

## 🚀 Uso recomendado

✔ Senhas
✔ Tokens de autenticação
✔ Links seguros
✔ Qualquer contexto que exija imprevisibilidade

---

## 📚 Referência

https://docs.python.org/pt-br/3/library/secrets.html
