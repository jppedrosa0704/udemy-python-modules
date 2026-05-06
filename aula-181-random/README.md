# 🎲 Uso do módulo `random` em Python

Este projeto demonstra o uso do módulo padrão `random` da linguagem Python para geração de números pseudoaleatórios e manipulação de listas.

## ⚠️ Importante

Os números gerados pelo módulo `random` são **pseudoaleatórios**, ou seja:

* Parecem aleatórios
* Mas são determinísticos (podem ser reproduzidos com a mesma entrada)

Por esse motivo, **não devem ser usados para segurança ou criptografia**.

---

## 📦 Módulo utilizado

```python
import random
```

---

## 🌱 Inicialização (seed)

```python
random.seed(0)
```

* Inicializa o gerador de números pseudoaleatórios
* Garante resultados reproduzíveis

---

## 🔢 Geração de números

### ▶️ `random.randrange(início, fim, passo)`

```python
r_range = random.randrange(10, 20, 2)
```

* Gera um número inteiro dentro de um intervalo com passo
* Exemplo: 10, 12, 14, 16, 18

---

### ▶️ `random.randint(início, fim)`

```python
r_int = random.randint(10, 30)
```

* Gera um número inteiro entre início e fim (inclusive)

---

### ▶️ `random.uniform(início, fim)`

```python
r_uniform = random.uniform(10, 20)
```

* Gera um número decimal (float) dentro do intervalo

---

## 🔀 Manipulação de listas

```python
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
```

---

### 🔄 `random.shuffle(lista)`

```python
random.shuffle(nomes)
```

* Embaralha os elementos da lista original
* Modifica a lista diretamente

---

### 🎯 `random.sample(iterável, k=N)`

```python
novos_nomes = random.sample(nomes, k=3)
```

* Retorna uma nova lista com elementos escolhidos
* Não repete valores
* Não altera a lista original

---

### 🔁 `random.choices(iterável, k=N)`

```python
novos_nomes = random.choices(nomes, k=3)
```

* Retorna uma nova lista com elementos escolhidos
* Pode repetir valores

---

### 👤 `random.choice(iterável)`

```python
random.choice(nomes)
```

* Retorna um único elemento aleatório da lista

---

## 📌 Resumo

| Função    | Descrição                   |
| --------- | --------------------------- |
| seed      | Inicializa o gerador        |
| randrange | Inteiro com passo           |
| randint   | Inteiro (intervalo fechado) |
| uniform   | Número decimal              |
| shuffle   | Embaralha lista             |
| sample    | Seleção sem repetição       |
| choices   | Seleção com repetição       |
| choice    | Um único elemento           |
