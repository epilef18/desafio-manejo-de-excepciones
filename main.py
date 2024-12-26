from foto import Foto
from error import DimensionError

def ingresar_medidas():
    ancho = int(input("Ingrese el ancho de la foto:"))
    alto = int(input("Ingrese el ancho de la foto:"))
    return ancho, alto

def main():
    try:
        ancho, alto = ingresar_medidas()
        ruta = "c/.../imagen.jpg"
        foto1 = Foto(ancho, alto, ruta)
        print("Foto creada con éxito.")
        
        nuevo_ancho = int(input("Ingresa un nuevo ancho para la foto: "))
        foto1.ancho = nuevo_ancho

        nuevo_alto = int(input("Ingresa un nuevo alto para la foto: "))
        foto1.alto = nuevo_alto

    except DimensionError as e:
        print(e)

if __name__ == "__main:__":
    main()