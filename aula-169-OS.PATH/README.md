# 📘 Trabalhando com caminhos de arquivos usando `os.path` no Python

Este exemplo demonstra como utilizar o módulo **`os.path`** para manipular caminhos de arquivos de forma segura e compatível com **Windows, Linux e macOS**. O módulo `os.path` abstrai as diferenças entre sistemas operacionais, permitindo construir, dividir e analisar caminhos sem se preocupar com barras (`/` ou `\`).

---

## 🧩 O que o código demonstra

### **1. Construção de caminhos com `os.path.join()`**
Cria caminhos corretos para qualquer sistema operacional:

```python
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')

Linux/macOS → Desktop/curso/arquivo.txt

Windows → Desktop\curso\arquivo.txt

2. Separar diretório e arquivo com os.path.split()
python
diretorio, arquivo = os.path.split(caminho)
Retornos:

diretorio → 'Desktop/curso'

arquivo → 'arquivo.txt'

3. Separar nome e extensão com os.path.splitext()
python
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
Retornos:

nome_arquivo → 'arquivo'

extensao_arquivo → '.txt'

4. Obter apenas o diretório com os.path.dirname()
python
os.path.dirname(caminho)
Retorna:

Código
Desktop/curso

🎯 Objetivo do exercício
Entender como o módulo os.path manipula caminhos de forma multiplataforma.

Construir caminhos sem depender do sistema operacional.

Extrair diretórios, nomes de arquivos e extensões.

Verificar e analisar caminhos de forma segura.
