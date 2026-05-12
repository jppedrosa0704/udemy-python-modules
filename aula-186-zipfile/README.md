# 📦 ZIP – Compactando e Descompactando Arquivos com `zipfile.ZipFile`

Este projeto demonstra como **criar arquivos**, **compactar**, **listar** e **descompactar** conteúdos utilizando o módulo `zipfile.ZipFile` da biblioteca padrão do Python.  
Também utiliza `os`, `shutil` e `pathlib` para manipulação de diretórios e arquivos.

---

## 🗂️ Estrutura do Script

O script realiza as seguintes etapas:

### 1. **Definição de Caminhos**
Utiliza `Path(__file__).parent` para trabalhar sempre no diretório do script.

### 2. **Limpeza de diretórios antigos**
Remove:
- pasta de origem dos arquivos
- arquivo `.zip` anterior
- pasta descompactada

Usa:
- `shutil.rmtree()`
- `Path.unlink()`

### 3. **Criação de Arquivos de Exemplo**
A função:

```python
def criar_arquivos(qtd: int, zip_dir: Path):

📦 Compactando Arquivos
O bloco:

python
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip.write(os.path.join(root, file), file)
Cria o arquivo aula186_compactado.zip

Adiciona todos os arquivos da pasta criada

Usa os.walk() para percorrer diretórios

📃 Lendo o Conteúdo do ZIP
python
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
Lista todos os arquivos dentro do ZIP

namelist() retorna os nomes dos arquivos compactados

📂 Descompactando Arquivos
python
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
Extrai tudo para a pasta aula186_descompactado

🚀 Tecnologias Utilizadas
Python 3.x

zipfile.ZipFile

pathlib.Path

os

shutil

📘 Objetivo
Este exemplo serve como referência para:

Criar arquivos dinamicamente

Compactar diretórios

Ler conteúdo de arquivos ZIP

Descompactar arquivos

Automatizar rotinas de backup e organização
