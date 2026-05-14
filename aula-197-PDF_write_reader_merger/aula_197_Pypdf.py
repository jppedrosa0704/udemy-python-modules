# from pathlib import Path

# from PyPDF2 import PdfReader

# PASTA_RAIZ = Path(__file__).parent
# PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
# PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

# RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20260508.pdf'

# PASTA_NOVA.mkdir(exist_ok=True)

# reader = PdfReader(RELATORIO_BACEN)

# # print(len(reader.pages))
# # for page in reader.pages:
# #     print(page)
# #     print()

# page0 = reader.pages[0]
# imagem0 = page0.images[0]

# # print(page0.extract_text())
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

from pathlib import Path
from pypdf import PdfReader, PdfWriter
from PyPDF2 import PdfMerger
from PIL import Image
from io import BytesIO

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20260508.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

page0 = reader.pages[0]
imagem0 = page0.images[0]

# bytes da imagem
dados = imagem0.data

# abre com Pillow
img = Image.open(BytesIO(dados))

# converte se necessário
if img.mode == 'PA':
    img = img.convert('RGBA')

# salva
img.save(PASTA_NOVA / 'imagem0.png')



#############################################

# writer = PdfWriter()
# writer.add_page(page0)

# with open(PASTA_NOVA / 'page0.pdf', 'wb') as arquivo:
#     writer.write(arquivo)

# with open(PASTA_NOVA / 'novo_pdf.pdf', 'wb') as arquivo:
#     for page in reader.pages:
#         writer.add_page(page)
        
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f"page{i}.pdf", 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo) #type: ignore


files = [
    PASTA_NOVA / "page0.pdf",
    PASTA_NOVA / "page1.pdf"
]

merger = PdfMerger()

for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'merged.pdf')
merger.close()



