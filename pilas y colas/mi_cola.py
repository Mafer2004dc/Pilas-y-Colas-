from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del frente al final -------
    def desencolar(self):
        if self.cantidaad == 0:
            print("  ⚠ La cola está vacía")
            return None
        salida = self.datos[0]  # el FRENTE es el primero que llegó
        for i in range(1, self.cantidad):  # 1, 2
            self.datos[i - 1] = self.datos[i]  # se "corre" hacia adelante
        self.datos[self.cantidad - 1] = None  # se "elimina" del arreglo
        self.cantidad = self.cantidad - 1
        return salida

    def ver_frente(self):
        if self.cantidad == 0:
            print("  ⚠ La cola está vacía")
            return None
        return self.datos[0]  # el FRENTE es el primero que llegó

    def buscar(self, numero):
        for i in range(self.cantidad):  # del FRENTE al FINAL
            if self.datos[i].numero == numero:
                return self.datos[i]
        print("  ⚠ No se encontró el pasajero")
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        for i in range(self.cantidad):  # del FRENTE al FINAL
            if self.datos[i].numero == numero:
                self.datos[i].destino = nuevo_destino
                self.datos[i].asiento = nuevo_asiento
                print("  ✓ Pasajero modificado")
                return True
        print("  ⚠ No se encontró el pasajero")
        return False

    def eliminar_por_numero(self, numero):
        total= self.cantidad
        encontrado = False
        for i in range(total):
            pasajero = self.desencolar()
            if pasajero.numero == numero:
                encontrado = True
                print("  ✓ Pasajero eliminado")
            else:
                self.encolar(pasajero)

    def copiar(self):
        nueva_cola = MiCola(self.capacidad)
        for i in range(self.cantidad):  # del FRENTE al FINAL
            nueva_cola.encolar(self.datos[i])
        return nueva_cola

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0