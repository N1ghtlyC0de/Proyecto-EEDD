
import time
from DataStructures.avltree import AVLTree

if __name__ == '__main__':
    # Método Número 2
    with open("D:\Academico\Estructura de Datos\EDD\Proyecto Estructuras\cienmil_elementos.txt", "r") as fileData:
        data = fileData.readlines()

    avl_tree = AVLTree()
    # INSERCIÓN DE DATOS
    for line in data:
        line = line.strip()
        olx = line.split(", ")
        avl_tree.insert(olx[0].strip())
    #BUSQUEDA DEL ELEMENTO
    element = input("Ingrese el elemento: ")

    start_time = time.time()

    node= avl_tree.search(element)
    if node is not None:
        print("Elemento encontrado:", node.key)
    else:
        print("Elemento no encontrado")

    end_time = time.time()
    print("Tiempo de ejecución:", end_time - start_time, "segundos")





