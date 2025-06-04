# utils/io_handler.py
import ast

def get_matrix_input(prompt):
    """
    Recibe entrada como texto representando una matriz, por ejemplo: [[1,2],[3,4]]
    """
    try:
        return ast.literal_eval(input(prompt))
    except Exception:
        raise ValueError("Formato inválido. Usa algo como: [[1,2],[3,4]]")

def get_vector_input(prompt):
    """
    Recibe entrada como valores separados por espacio y los convierte a lista de floats
    """
    try:
        return list(map(float, input(prompt).strip().split()))
    except Exception:
        raise ValueError("Vector inválido. Usa algo como: 1 2 3")

def get_number_input(prompt):
    """
    Recibe un número como string y lo convierte a float
    """
    try:
        return float(input(prompt))
    except Exception:
        raise ValueError("Entrada no válida. Debe ser un número.")