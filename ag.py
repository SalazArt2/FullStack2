import numpy as np
import cv2
from PIL import Image

class Red:
    # Entradas y Salidas
    N = 10 #entradas
    M = 2 #salidas
    Gamma = 0.5
    ClasesUsadas = 0
    Vigilancia = 0.8

    # Cambios en el constructor  !!!!!!!
    # Almacen de Entradas en Clases cuando desvordan
    Clases = [
        # Clase 0
        [],
        # Clase 1
        []
    ]

    def __init__(self, N=4, M=2, Gamma='0.5', Vigilancia='0.8'):
        self.N = N
        self.M = int(M)
        self.Gamma = Gamma
        self.Vigilancia = Vigilancia

        valorW = 1 / (1 + self.N) 
        self.V = np.full((self.M, self.N), 1)
        self.W = np.full((self.N, self.M), valorW)

      

    def Set(self, Gamma='0.5', Vigilancia='0.8'):
        self.Gamma = Gamma
        self.Vigilancia = Vigilancia

    # Método Principal
    def calcular(self, entrada):
        print(entrada)
        ganadora = self.compentencia(entrada)
        numNeuro = int(ganadora[0])
        # Comprobar límite de Salidas
        if self.ClasesUsadas >= self.M:
            print('-------------------')
            # Prueba de semejanza
            if self.semejanza(entrada, numNeuro, False):
                # Si la pasa pertenece a la clase y la anterior entrada se guarda en el registro de clases
                self.agregarRegistro(numNeuro)
                print(f'Prueba de Semejansa pasada entra en la clase {numNeuro}')
            else:
                # Si no la pasa crea una nueva salida/clase
                print('Saturacion de la red se crea nueva salida')
                self.agregarSalida()
                # Cambia la clase a la que pertenece y modifica los pesos
                ganadora[0] = self.M - 1
                self.modificar_pesos(entrada, ganadora)
        else:
            self.modificar_pesos(entrada, ganadora)

        return self.salida(numNeuro)

    def concindencia(self, entrada):
        res = []

        for i in range(self.M):
            res.append([i, self.semejanza(entrada, i, True)])

        res = np.array(res)
        res = res[np.argsort(-res[:, 1])]

        return res

    def compentencia(self, entrada):
        print("--------------------")
        print(f"Competencia  : \n")

        suma = []

        for j in range(len(self.W[0])):
            suma.append([j, np.sum(entrada * self.W[:, j])])

        suma = np.array(suma)

        # Ordenar la suma por el valor de la suma acumulada
        suma_ordenada = suma[np.argsort(-suma[:, 1])]
        print(f"Resultado de Competencia : \n {suma_ordenada}")
        ganadora = suma_ordenada[0]
        print("--------------------")
        print(f"Neurona ganadora : {ganadora}")

        return ganadora

    def modificar_pesos(self, entrada, ganadora):
        print("--------------------")
        print("Modificacion de Peso:")

        # Actualizacion de V
        numNeurona = int(ganadora[0])
        antigua = self.V[numNeurona].copy()
        self.V[numNeurona] = ((self.V[numNeurona].astype(bool)) & (entrada.astype(bool))).astype(int)

        print("\nMatriz V:")
        print(self.V)

        # Actualizar W
        sumaGamma = (self.Gamma + np.sum(antigua * self.V[int(numNeurona)]))
        self.W[:, numNeurona] = self.V[numNeurona] * antigua / sumaGamma

        print("\nMatriz W:")
        print(self.W)

        self.ClasesUsadas += 1

    def semejanza(self, entrada, numNeurona, type):
        relacion = np.sum(entrada * self.V[numNeurona]) / np.sum(entrada)

        if type:
            return relacion
        else:
            print("--------------------")
            print( f'Prueba de semejanza relacion : {relacion} de {self.Vigilancia}')
            return self.Vigilancia < relacion

    def agregarSalida(self):
        self.V = np.vstack([self.V, np.full(self.N, 1)])
        self.W = np.hstack([self.W, np.full((self.N, 1), 1)])

        self.M += 1
        self.Clases.append([])

        self.mostratVW()

    def agregarRegistro(self, num):
        self.Clases[num].append(self.V[num].tolist())

    def mostrarClases(self):
        i = 1
        for clase in self.Clases:
            print(f'\n Clase {i} : {clase}')
            i += 1

    def mostratVW(self):
        print("\nMatriz V:")
        print(self.V)
        print("\nMatriz W:")
        print(self.W)

    def mostrarParametros(self):
        print(f'N = {self.N}')
        print(f'M = {self.M}')
        print(f'Vigilancia = {self.Vigilancia}')
        print(f'Gamma = {self.Gamma}')

    def salida(self, num):
        return self.V[num]

    def get_numero_clases(self):
        return self.ClasesUsadas

    def transformarImagen(self, dirImagen):
        with Image.open(dirImagen) as img:
            img = img.convert('L')  # Convertir a escala de grises
            img = img.resize((50, 50))  # Ajustar el tamaño a 50x50
            img_array = np.array(img)
            img_array = (img_array > 128).astype(int)  # Convertir a binario (0 o 1)
            return img_array.flatten()

