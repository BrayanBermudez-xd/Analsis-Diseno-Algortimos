import re

def analizar_codigo(codigo):
    lineas = codigo.split("\n")
    
    pila = []
    max_anidacion = 0
    logaritmico = False
    
    print("\n--- Análisis Línea por Línea ---\n")
    
    for num, linea in enumerate(lineas, start=1):
        linea_limpia = linea.strip()
        
        if not linea_limpia:
            continue

        indent = len(linea) - len(linea.lstrip())

        # Ajustar pila según indentación
        while pila and indent <= pila[-1]:
            pila.pop()

        tipo = "O(1)"

        # Detectar for
        if linea_limpia.startswith("for "):
            pila.append(indent)
            max_anidacion = max(max_anidacion, len(pila))
            tipo = "O(n)"

        # Detectar while
        elif linea_limpia.startswith("while "):
            pila.append(indent)
            max_anidacion = max(max_anidacion, len(pila))
            tipo = "O(n) o depende de condición"

        # Detectar logaritmo
        if re.search(r"//= *2|/= *2", linea_limpia):
            logaritmico = True
            tipo = "O(log n)"

        print(f"Línea {num}: {tipo} → {linea_limpia}")

    # Determinar complejidad final
    if logaritmico and max_anidacion == 1:
        total = "O(log n)"
    elif logaritmico and max_anidacion >= 2:
        total = "O(n log n)"
    elif max_anidacion == 0:
        total = "O(1)"
    elif max_anidacion == 1:
        total = "O(n)"
    else:
        total = f"O(n^{max_anidacion})"

    print("\n--- Complejidad Total Estimada ---")
    print(total)

#Aqui el usuario proporciona el codigo que desea analizar para sacar la notacion Big O
if __name__ == "__main__":
    print("Agrega el codigo para analizarlo (escribe 'FIN' para analizarlo):\n")
    
    codigo_usuario = ""
    while True:
        linea = input()
        if linea.strip().upper() == "FIN":
            break
        codigo_usuario += linea + "\n"

    analizar_codigo(codigo_usuario)
