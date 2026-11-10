from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

   
    
    def apilar(self, pasajero):                      # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantdad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        if self.cantidad == 0:
            print("  ⚠ La pila está vacía")
            return None
        salida = self.datos[self.cantidad - 1]  # el TOPE es el último que entró
        self.datos[self.cantidad - 1] = None     # se "elimina" del arreglo
        self.cantidad = self.cantidad - 1    #uno menos 
        return salida 

    def ver_tope(self):
        if self.cantidad == 0:
            print("  ⚠ La pila está vacía")
            return None
        return self.datos[self.cantidad - 1]  # el TOPE es el último que entró

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):  # del TOPE al FONDO
            if self.datos[i].numero == numero:
                return self.datos[i]
        print("  ⚠ No se encontró el pasajero")
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posision = self.buscar(numero)
        if posision == -1:
            return False
            posision.destino = nuevo_destino
            posision.asiento = nuevo_asiento
            print("  ✓ Pasajero modificado")
            return True

    def eliminar_por_numero(self, numero):
        aux = self.buscar(numero)
        encontrado = False
        while self.cantidad > 0 and not encontrado:
            pasajero = self.desapilar()
            if pasajero.numero == numero:
                encontrado = True
                print("  ✓ Pasajero eliminado")
            else:
                self.apilar(pasajero)

    def copiar(self):
        nueva_pila = MiPila(self.capacidad)
        for i in range(self.cantidad - 1, -1, -1):  # del TOPE al FONDO
            nueva_pila.apilar(self.datos[i])
        return nueva_pila

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0