import sys
import io
import contextlib

def run_python_code(code: str) -> str:
    output = io.StringIO()
    local_vars = {} 
    
    try:
        with contextlib.redirect_stdout(output):
            exec(code, {"__builtins__": __import__("builtins")}, local_vars)
        result = output.getvalue()
        return result if result else "Kód úspešne prebehol, ale nevygeneroval žiadny textový výstup."
    except Exception as e:
        return f"Chyba pri vykonávaní kódu: {str(e)}"