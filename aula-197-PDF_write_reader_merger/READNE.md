Manipulação de PDFs com Python

Projeto simples demonstrando como:

Ler arquivos PDF
Extrair imagens de páginas
Salvar páginas separadamente
Mesclar PDFs
Trabalhar com imagens usando Pillow
Tecnologias utilizadas
Python 3
pypdf
PyPDF2
Pillow
Estrutura do projeto
project/
│
├── pdfs_originais/
│   └── R20260508.pdf
│
├── arquivos_novos/
│
└── main.py
Instalação

Clone o repositório:

git clone <url-do-repositorio>

Entre na pasta:

cd nome-do-projeto

Instale as dependências:

pip install pypdf PyPDF2 pillow
Funcionalidades
1. Ler um PDF
from pypdf import PdfReader

reader = PdfReader("arquivo.pdf")
2. Extrair imagem do PDF

O código pega a primeira imagem da primeira página:

page0 = reader.pages[0]
imagem0 = page0.images[0]

Depois salva como PNG usando Pillow.

3. Separar páginas em PDFs individuais

Cada página é salva em um arquivo diferente:

for i, page in enumerate(reader.pages):
    writer = PdfWriter()

    with open(f"page{i}.pdf", "wb") as arquivo:
        writer.add_page(page)
        writer.write(arquivo)
4. Mesclar PDFs

Exemplo usando PdfMerger:

from PyPDF2 import PdfMerger

files = [
    "page0.pdf",
    "page1.pdf"
]

merger = PdfMerger()

for file in files:
    merger.append(file)

merger.write("merged.pdf")
merger.close()
Resultado

O projeto gera:

imagens extraídas do PDF
páginas separadas em PDFs individuais
um novo PDF mesclado

Tudo salvo na pasta:

arquivos_novos/
Observações

O PdfMerger também pode ser importado diretamente do pypdf:

from pypdf import PdfMerger

Dependendo da versão instalada, isso pode evitar incompatibilidades entre pypdf e PyPDF2.

Autor

Projeto para estudos de manipulação de PDFs com Python.
