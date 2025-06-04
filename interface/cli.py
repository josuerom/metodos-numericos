def main_menu():
    from utils.io_handler import get_matrix_input, get_vector_input, get_number_input
    import numpy as np

    while True:
        print("==== MATRIX CALC MÉTODOS NUMÉRICOS ====")
        print("1. Gauss")
        print("2. Lu")
        print("3. Jacobi")
        print("4. Interpolación")
        print("5. Derivación")
        print("6. Integración")
        print("7. EDO")
        print("8. Exportar historial")
        print("0. Salir")
        op_1 = input(">> ")

        if op_1 == "1":
            from core.gauss import gauss_elimination
            A = get_matrix_input("Matriz.   Ej: [[2,1],[5,7]]: ")
            b = get_vector_input("Términos. Ej: 11 13: ")
            x, steps = gauss_elimination(np.array(A), np.array(b))
            for step in steps:
                print(step)
            print("Resultado:", x)

        elif op_1 == "2":
            from core.lu import lu_decomposition
            A = get_matrix_input("Matriz. Ej: [[4,3],[6,3]]: ")
            (P, L, U), exp = lu_decomposition(np.array(A))
            print(exp)
            print("L =", L)
            print("U =", U)

        elif op_1 == "3":
            from core.jacobi import jacobi_method
            A = get_matrix_input("Matriz.   Ej: [[4,1],[2,3]]: ")
            b = get_vector_input("Términos. Ej: 1 2: ")
            x, steps = jacobi_method(np.array(A), np.array(b))
            for step in steps:
                print(step)
            print("Resultado:", x)

        elif op_1 == "4":
            from core.interpolation import interpolate_lagrange
            x = get_vector_input("Valores de x separados por espacio. Ej: 1 2 3: ")
            y = get_vector_input("Valores de y separados por espacio. Ej: 2 3 5: ")
            poly, exp = interpolate_lagrange(x, y)
            print(exp)
            print("Polinomio resultante:\n", poly)

        elif op_1 == "5":
            from core.differentiation import numerical_derivative
            f_expr = input("Función f(x).  Ej: x**2: ")
            x_val = get_number_input("Valor de x para derivar: ")
            df, exp = numerical_derivative(f_expr, x_val)
            print(exp)
            print(f"Derivada en x={x_val}:", df)

        elif op_1 == "6":
            from core.integration import numerical_integration
            f_expr = input("Función f(x). Ej: -1/x**2): ")
            a = get_number_input("Límite inferior a: ")
            b = get_number_input("Límite superior b: ")
            result, exp = numerical_integration(f_expr, a, b)
            print(exp)
            print(f"Integral de f(x) en [{a}, {b}]:", result)

        elif op_1 == "7":
            from core.edo import solve_ode
            f_expr = input(       "Función f(t, y). Ej: t*y-2: ")
            t0 = get_number_input("Tiempo inicial t0: ")
            tf = get_number_input("  Tiempo final tf: ")
            y0 = get_number_input("Condición inicial y0: ")
            sol, exp = solve_ode(f_expr, t0, tf, y0)
            print(exp)
            print("Resultado de la EDO:", sol.y)

        elif op_1 == "8":
            from utils.exporter import export_history_to_pdf
            export_history_to_pdf()
            print("Se acaba de exportar el archivo PDF con el historial de las consultas.")

        elif op_1.lower() in ["salir", "exit", "quit"]:
            print("Saliendo del programa.")
            break
        elif op_1 == "0":
            print("Saliendo del programa.")
            break
        else:
            print("*****\nOpción inválida. Doctor/a intente de nuevo.\n*****")

        op_2 = input("\n¿Desea continuar probando este programa? ")
        if op_2.lower() not in ["s", "si", "yes", "claro", "que si", "de eso dependo"]:
            break