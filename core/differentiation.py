from utils.explainer import explain_step
from database.db import save_result

def numerical_derivative(f_expr, x, h=1e-5):
    try:
        f = eval(f"lambda x: {f_expr}")
    except Exception as e:
        raise ValueError(f"Error al procesar la función: {e}")
    
    df = (f(x + h) - f(x - h)) / (2 * h)
    explanation = explain_step(x, h, df, 'derivative')
    save_result("Derivación", f"f(x)={f_expr}, x={x}", df, explanation)
    return df, explanation