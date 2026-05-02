# 📁 Copiando Arquivos e Pastas com `os` + `shutil` em Python

Este README explica de forma clara e direta como o script funciona para **copiar uma estrutura completa de diretórios** (pastas + arquivos) de um local para outro usando os módulos `os` e `shutil`.

---

## 🧠 Objetivo do Script
O código copia **todas as pastas e arquivos** dentro de uma pasta original (`PASTA_ORIGINAL`) para uma nova pasta (`NOVA_PASTA`) mantendo **a mesma estrutura de diretórios**.

---

## 📦 Módulos Utilizados

- **os** → manipulação de caminhos, diretórios e navegação.
- **shutil** → operações de cópia de arquivos.

---

## 🗂️ Como o Script Funciona

### 1. Descobre o diretório HOME do usuário
```python
HOME = os.path.expanduser('~')
2. Exemplo no Windows:
C:\Users\jp-pe

DESKTOP = os.path.join(HOME, 'Desktop')

3. Define:
PASTA_ORIGINAL → pasta que será copiada

NOVA_PASTA → destino da cópia

PASTA_ORIGINAL = os.path.join(DESKTOP, 'joaopaulo')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
os.makedirs(NOVA_PASTA, exist_ok=True)

🔄 4. Percorre toda a estrutura com os.walk
os.walk retorna:

root → pasta atual

dirs → subpastas

files → arquivos

📁 5. Cria as pastas no destino
for dir_ in dirs:
    caminho_novo_diretorio = os.path.join(
        root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
    )
    os.makedirs(caminho_novo_diretorio, exist_ok=True)

📄 6. Copia cada arquivo para o novo local
python
for file in files:
    caminho_arquivo = os.path.join(root, file)
    caminho_novo_arquivo = os.path.join(
        root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
    )
    shutil.copy(caminho_arquivo, caminho_novo_arquivo)
shutil.copy copia o arquivo mantendo:

nome

conteúdo

✅ Resultado Final
Ao final da execução, você terá:

Código
NOVA_PASTA/
│
├── (todas as subpastas de joaopaulo)
│   ├── ...
│   └── ...
└── (todos os arquivos copiados)
A estrutura é idêntica à original.

📝 Pontos Importantes
O script não sobrescreve pastas, mas sobrescreve arquivos se já existirem.

os.walk garante que tudo seja percorrido recursivamente.

shutil.copy copia apenas arquivos, não pastas (por isso criamos as pastas antes).

🚀 Conclusão
Este script é uma forma segura e eficiente de copiar uma árvore de diretórios inteira usando apenas módulos nativos do Python.
Ideal para backups, organização de arquivos ou duplicação de projetos.
