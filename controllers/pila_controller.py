from flask import Blueprint, jsonify, request
from models.pila import pila, nodo_simple

main = Blueprint("pila_bp", __name__)

@main.route("/pila/calcular", methods=["POST"])
def calcular_expresion():
    data = request.json
    expresion = data.get("expresion", "")

    # Pilas principales
    pila_numeros = pila()
    pila_operadores = pila()
    # Variables auxiliares
    numero_actual = ""
    # Separar números y operadores de la expresión
    for char in expresion:
        if char.isdigit():
            numero_actual += char
        else:
            if numero_actual != "":
                pila_numeros.push(nodo_simple(int(numero_actual)))
                numero_actual = ""
            if char in "+-*/":
                pila_operadores.push(nodo_simple(char))
    if numero_actual != "":
        pila_numeros.push(nodo_simple(int(numero_actual)))
    # Evaluar expresión (de izquierda a derecha)
    def pila_a_lista_en_orden(p):
        arr = []
        actual = p.cabeza
        while actual:
            arr.append(actual.dato)
            actual = actual.siguiente
        return arr[::-1]  # invertir para recuperar orden original
    numeros = pila_a_lista_en_orden(pila_numeros)
    operadores = pila_a_lista_en_orden(pila_operadores)
    if len(numeros) == 0:
        return jsonify({"error": "No hay operandos"}), 400
    resultado = numeros[0]
    i_num = 1
    i_op = 0
    while i_op < len(operadores) and i_num < len(numeros):
        signo = operadores[i_op]
        operando = numeros[i_num]
        if signo == "+":
            resultado += operando
        elif signo == "-":
            resultado -= operando
        elif signo == "*":
            resultado *= operando
        elif signo == "/":
            if operando == 0:
                return jsonify({"error": "División por cero"}), 400
            resultado /= operando
        i_op += 1
        i_num += 1
    # Crear pila_concatenacion (primero operadores, luego operandos)
    pila_concatenacion = pila()
    # Primero vaciar pila_operadores
    for signo in operadores:
        pila_concatenacion.push(nodo_simple(signo))
    # Luego vaciar pila_numeros
    for num in numeros:
        pila_concatenacion.push(nodo_simple(num))
    # Devolver todo
    return jsonify({
        "expresion_recibida": expresion,
        "pila_operadores": operadores,
        "pila_numeros": numeros,
        "pila_concatenacion": pila_concatenacion.to_JSON(),
        "resultado": resultado
    }), 200
