import requests

def explain_step(*args, method='gauss'):
    prompt_map = {
        'gauss': f"Explica matemáticamente el paso a paso completo de la eliminación Gaussiana para: {args}",
        'lu': f"Explica matemáticamente el paso a paso completo y breve de la descomposición LU para: {args}",
        'jacobi': f"Explica matemáticamente el paso a paso completo de la iteración Jacobi para {args[2]}: x nuevo = {args[1]} partiendo de {args[0]}",
        'lagrange': f"Explica matemáticamente el paso a paso completo para la interpolación de Lagrange sobre puntos: {args[0]} y {args[1]}",
        'derivative': f"Explica matemáticamente el paso a paso completo para el calculo de la derivada numérica en x={args[0]}, h={args[1]}, resultado={args[2]}",
        'integration': f"Explica matemáticamente el paso a paso completo para la integración numérica entre {args[0]} y {args[1]}, resultado={args[2]}",
        'ode': f"Explica matemáticamente el paso a paso completo para la solución de EDO con condiciones iniciales {args[1]} en el intervalo {args[0]}"
    }
    prompt = prompt_map.get(method, f"Explica matemáticamente el paso a paso completo para el procedimiento del método {method} con datos: {args}")
    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": "Bearer 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"},
            json={
                "model": "deepseek-math",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        return response.json()["choices"][0]["message"]["content"]
    except:
        return f"[\nAsistente matemático: {prompt}\n]"