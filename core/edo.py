from scipy.integrate import solve_ivp
from utils.explainer import explain_step
from database.db import save_result

def solve_ode(f_expr, t0, tf, y0):
    try:
        f = eval(f"lambda t, y: {f_expr}")
    except Exception as e:
        raise ValueError(f"Error al procesar la función: {e}")
    
    sol = solve_ivp(f, (t0, tf), [y0])
    explanation = explain_step((t0, tf), y0, sol.y, 'ode')
    save_result("EDO", f"f(x)={f_expr}, t0={t0}, tf={tf}, y0={y0}", sol, explanation)
    return sol, explanation
