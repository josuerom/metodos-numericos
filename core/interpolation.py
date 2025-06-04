import numpy as np
from scipy.interpolate import lagrange
from utils.explainer import explain_step
from database.db import save_result

def interpolate_lagrange(x, y):
    poly = lagrange(x, y)
    explanation = explain_step(x, y, 'lagrange')
    save_result("Intepolación", f"x={x}, y={y}", poly, explanation)
    return poly, explanation