
class Ventas:
    __importe: float

    def __init__(self, importe):
        self.__importe= importe
        
    def get_importe(self):
        return self.__importe
    
    def set_importe(self, nuevo):
        nuevo= self.__importe
        return nuevo
    