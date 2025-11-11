class nodo_simple:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def __str__(self):
        return str(self.dato)

    def to_JSON(self):
        return {
            'dato': self.dato,
            'siguiente': self.siguiente.dato if self.siguiente else None
        }


class pila:

    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def push(self, nuevo_nodo):
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.longitud += 1

    def pop(self):
        if self.cabeza is None:
            print("la pila esta vacia")
            return
        valor = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self.longitud -= 1
        return valor

    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos)

    def to_JSON(self):
        lista = []
        actual = self.cabeza
        while actual is not None:
            lista.append(actual.to_JSON())
            actual = actual.siguiente
        return lista

"""pila = pila()
nodo1 = nodo_simple(1)
nodo2 = nodo_simple(2)
nodo3 = nodo_simple(3)
nodo4 = nodo_simple(4)
nodo5 = nodo_simple(5)
nodo6 = nodo_simple(6)


pila.push(nodo1)
pila.push(nodo2)
pila.push(nodo3)
pila.push(nodo4)
pila.push(nodo5)
pila.push(nodo6)
print(pila)

pila.pop()
print(pila)

print(pila.to_JSON())"""