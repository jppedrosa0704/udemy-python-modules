# Python Module Example – Understanding `if __name__ == "__main__"`

This repository contains a simple and clear example demonstrating how Python modules work, how to import functions from another file, and how the `if __name__ == "__main__"` block controls script execution.

## 📌 Project Structure


## 📘 Description
- `modulo.py` defines the function `soma(x, y)` that performs a simple addition.
- `entendendo_if_name_==_main__.py` imports the function and also defines its own version of `soma` to illustrate namespace separation.
- The script uses `if __name__ == "__main__"` to run code only when the file is executed directly, not when imported.

## ▶️ How It Works

### Importing the function
```python
from modulo import soma
print(soma(1, 3))
