class Stacks:
    def __init__(self, listaInicial):
        self.items = listaInicial

    def estaVacia(self):
        return self.items == []

    def incluir(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items) - 1]

    def tamano(self):
        return len(self.items)

class Queues:
    def __init__(self, listaInicial):
        self.items = listaInicial

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0



def main():
    listaInicial = ['casa', 'perro', 'gato', 'hombre', 'mujer', 'nino', 'tv', 'computador', 'teclado', 'mouse']

    respuesta = int(input('Bienvenido al programa, ingrese 1 si desea crear un stack e ingrese 2 si desea crear un queue, o ingrese -1 para terminar: '))
    print('La lista inicial es: ', listaInicial, '\n')

    if respuesta == 1:
        stack = Stacks(listaInicial)
        print('El stack es: ')
        for i in range(len(listaInicial) -1, -1, -1):
            print(stack.inspeccionar()) #retorna el ultimo elemento de la pila
            stack.extraer() #elimina el ultimo elemento de la pila para que en el siguiente ciclo no se repita

    elif respuesta == 2:
        queue = Queues(listaInicial)
        print('\nEl queue es: ')
        for i in range(len(listaInicial)):
            print(queue.desencolar()) #retorna el primer elemento de la cola y elimina su valor
    else:
        print('Gracias por usar el programa')


if __name__ == "__main__":
    main()