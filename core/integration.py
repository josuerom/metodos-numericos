from scipy.integrate import quad
from utils.explainer import explain_step
from database.db import save_result

def numerical_integration(f_expr, a, b):
    try:
        f = eval(f"lambda x: {f_expr}")
    except Exception as e:
        raise ValueError(f"Error al procesar la función: {e}")
    
    result, _ = quad(f, a, b)
    explanation = explain_step(a, b, result, 'integration')
    save_result("Integración", f"f(x)={f_exp}, a={a}, b={b}", result, explanation)
    return result, explanation
