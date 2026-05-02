# 📁 Manipulando Arquivos e Pastas com `os` e `shutil` em Python

Este documento explica como o script realiza operações de **cópia**, **remoção**, **movimentação** e **renomeação** de pastas e arquivos usando apenas módulos nativos do Python.

---

## 🧰 Módulos Utilizados

- **os** → manipulação de caminhos, diretórios e arquivos.
- **shutil** → operações de cópia, remoção e movimentação.

---

## 📌 Caminhos Principais

O script identifica automaticamente:

- **HOME** do usuário  
- **Área de Trabalho (Desktop)**  
- **Pasta original** a ser copiada  
- **Nova pasta** que será criada ou manipulada  

```python
HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'joaopaulo')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
```

---

## 📂 Operações Disponíveis

### 1. 🗑️ Apagar pastas recursivamente
Remove uma pasta inteira, incluindo subpastas e arquivos:

```python
shutil.rmtree(NOVA_PASTA)
```

### 2. 🗑️ Apagar arquivos individuais
Remove apenas arquivos:

```python
os.unlink(caminho_do_arquivo)
```

---

## 📄 Copiar Arquivos e Pastas

### 3. 📦 Copiar árvore de diretórios inteira
Copia a pasta original para a nova pasta:

```python
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
```

Isso cria `NOVA_PASTA` e copia tudo dentro de `joaopaulo`.

---

## 🔀 Mover ou Renomear Pastas

### 4. 🔁 Renomear usando `os.rename`
```python
os.rename(NOVA_PASTA, 'copia do joaopaulo')
```

### 5. 🚚 Mover ou renomear usando `shutil.move`
```python
shutil.move(NOVA_PASTA, NOVA_PASTA + 'copia do joao paulo')
```

`shutil.move` funciona para mover **ou** renomear, dependendo do destino.

---

## 🧠 Fluxo Completo do Script

1. Define caminhos  
2. Copia a pasta original para `NOVA_PASTA`  
3. Move ou renomeia a pasta copiada  

---

## ⚠️ Observações Importantes

- `copytree` **exige que a pasta destino NÃO exista**.  
- `rmtree` apaga tudo sem pedir confirmação.  
- `move` funciona tanto para mover quanto para renomear.  
- Se estiver usando **OneDrive**, erros de permissão podem ocorrer (WinError 5).  
- Para evitar problemas, prefira trabalhar fora do OneDrive.

---

## ✅ Conclusão

Este script demonstra como manipular arquivos e pastas de forma completa usando Python:

- Apagar  
- Copiar  
- Mover  
- Renomear  

Tudo com poucas linhas e usando apenas módulos nativos.

