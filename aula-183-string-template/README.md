# 📄 Template de Textos com Python (`string.Template`)

Este projeto demonstra como utilizar a classe `string.Template` do Python para gerar textos dinâmicos a partir de dados estruturados, como dicionários. Também inclui personalização de delimitadores e formatação de valores (como moeda e data).

---

## 🚀 Funcionalidades

* Substituição de variáveis em textos usando templates
* Diferença entre:

  * `substitute` (gera erro se faltar chave)
  * `safe_substitute` (ignora chaves ausentes)
* Criação de uma subclasse para alterar o delimitador padrão (`$` → `%`)
* Formatação de valores monetários (BRL)
* Manipulação de datas
* Leitura de template a partir de arquivo `.txt`

---

## 🧠 Conceitos Demonstrados

### 1. Uso básico do `string.Template`

```python
import string

template = string.Template("Olá, $nome!")
print(template.substitute(nome="João"))
```

---

### 2. Diferença entre `substitute` e `safe_substitute`

```python
template.substitute(dados)       # ERRO se faltar chave
template.safe_substitute(dados)  # NÃO gera erro
```

---

### 3. Criando um delimitador personalizado

```python
class MyTemplate(string.Template):
    delimiter = '%'
```

Agora você pode usar `%nome` em vez de `$nome` no seu template.

---

### 4. Formatação de moeda (BRL)

```python
def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl
```

---

### 5. Exemplo de dados usados

```python
dados = dict(
    nome='João',
    valor='R$ 1.234.567,00',
    data='06/05/2022',
    empresa='O.M.',
    telefone='+55 (81) 987096232'
)
```

---

## 📂 Estrutura do Projeto

```
📁 projeto/
│
├── main.py
├── aula_183.txt   # Template de texto
└── README.md
```

---

## 📝 Exemplo de Template (`aula_183.txt`)

```
Prezado(a) %nome,

Informamos que sua mensalidade será cobrada no valor de %valor no dia %data.
Caso deseje cancelar o serviço, entre em contato com a %empresa pelo telefone %telefone.

Atenciosamente,  
%empresa
```

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
```

2. Acesse a pasta:

```bash
cd seu-repo
```

3. Execute o script:

```bash
python main.py
```

---

## ⚠️ Observações

* Certifique-se de que o locale está configurado corretamente no seu sistema para formatação de moeda.
* O uso de `substitute` exige que todas as variáveis estejam presentes no dicionário.
* Use `safe_substitute` quando quiser evitar falhas por dados incompletos.

---

## 💡 Possíveis Melhorias

* Suporte a múltiplos idiomas
* Integração com envio de e-mails
* Interface web para preenchimento dos dados
* Validação automática de campos

---

## 📚 Referência

* Documentação oficial do Python:
  https://docs.python.org/3/library/string.html#template-strings

---

## 👨‍💻 Autor

Desenvolvido para fins de estudo e demonstração de templates em Python.
