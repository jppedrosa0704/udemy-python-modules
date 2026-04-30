# 📘 Uso do módulo `os` para interação com o sistema operacional

Este projeto demonstra como utilizar o módulo **`os`** do Python para executar comandos do sistema operacional diretamente a partir do código. O módulo `os` faz parte da biblioteca padrão e permite manipular diretórios, arquivos e processos do sistema.

---

## 🧩 Funcionalidades demonstradas

### **1. Limpar o terminal**
O comando para limpar o terminal varia conforme o sistema:

- **Windows (cmd antigo):** `cls`
- **Windows 11 (PowerShell), Linux e macOS:** `clear`

No código:

```python
os.system('cls')

Se estiveres no PowerShell, podes trocar por:

python
os.system('clear')
2. Executar comandos do sistema
O método os.system() envia comandos diretamente ao terminal.

Exemplo:

python
os.system('echo Hello World')
Isso imprime Hello World usando o comando do sistema, não o print() do Python.
