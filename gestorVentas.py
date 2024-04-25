from ventas import Ventas

class Gestor:
    __lista= [[]]

    def __init__(self):
        self.__lista=[]
        self.crearMatriz()  #ver como hacerlo privado para mayr seguridad
        
    def crearMatriz(self):
        filas = 5
        columnas = 7
         # Generar valores para cada celda
        contenido = 0  # Valor inicial
        for i in range(filas):
            fila = []            # Crear una nueva fila
            for j in range(columnas):
                fila.append(contenido)       # Agregar el valor del contador
                #contenido += 1           # Incrementar el contador
            self.__lista.append(fila)       # Agregar la fila a la matriz
        
        for fila in self.__lista:  # Imprimir la matriz
            print(fila)
    
    def agregarFactura(self, dia, suc, impor):
        self.__lista[suc-1][dia-1] += impor
        for fila in self.__lista:  # Imprimir la matriz
                 print(fila)
                 
    # -------ARREGLAR FUNCIONES DESDE ACÁ ----------------------

    def calculaTotalSuc(self, suc):
        total=0
        i=suc
        j=0
        for i in range(len(self.__lista[i])):
            for j in range(len(self.__lista[j])):
                total+= self.__lista[i][j].importe
                j+=1
        print("El total de facturación para la sucursal {} es de {} ",{suc}, {total}) 

    def sucursalMasFac(self, day):
        max=0
        i=0
        j=day
        for i in range(len(self.__lista[i])):
            for j in range(len(self.__lista[j])):
                if (self.__lista[i][j].importe > max):
                    max= self.__lista[i][j].importe
                    sucursal= i
            i+=1
        print("La sucursal {} es la que más facturó para el día {} ",{sucursal}, {day})    

    def menorFacSemanal(self):
        min=99999
        i=0
        j=0
        monto=0
        for i in range(len(self.__lista[i])):
            for j in range(len(self.__lista[j])):
                monto+= self.__lista[i][j].importe
                j+=1
            if (monto < min):
                    min= monto
            i+=1
        print("La sucursal que menos facturó por semana facturó un total de $ {} ",{min})
