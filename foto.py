import error 

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho > Foto.MAX or ancho < 1:
            raise error.DimensionError
        else:
            self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto > Foto.MAX or alto < 1:
            raise error.DimensionError
        else:
            self.__alto = alto
        