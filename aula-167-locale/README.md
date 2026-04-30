# 🌍 Aula — Usando `locale` para internacionalização em Python

Este diretório contém um exemplo prático de como utilizar o módulo interno `locale` em conjunto com o módulo `calendar` para gerar calendários formatados de acordo com a configuração regional do sistema.

O objetivo desta aula é demonstrar como:

- Ativar a localização (idioma e formatação) do sistema operacional  
- Exibir calendários completos com nomes de meses e dias traduzidos  
- Integrar `locale` com o módulo `calendar`  

---

# 🧠 Conceitos abordados

## 🔹 O módulo `locale`
O módulo `locale` permite que programas Python utilizem padrões regionais do sistema, como:

- Idioma  
- Formatação de datas  
- Formatação de números  
- Moedas  
- Nomes de meses e dias  

Ao usar:

```python
locale.setlocale(locale.LC_ALL, '')
