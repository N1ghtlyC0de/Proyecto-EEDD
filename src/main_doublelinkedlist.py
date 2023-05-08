from doubleLinkedList import DoubleLinkedList
import time
import random
start_time = time.time()

if __name__ == '__main__':
  with open("D:\Academico\Estructura de Datos\EDD\Proyecto Estructuras\onemillon_elementos.txt", "r") as fileData:
    data = fileData.readlines()

  list_of_data = DoubleLinkedList()
  list_of_compare_prices = DoubleLinkedList()
  for line in data:
    line.strip()
    olx = line.split(", ")
    list_of_data.append(olx[0], olx[1])
  
  with open('D:\Academico\Estructura de Datos\EDD\Proyecto Estructuras\serials_choice.txt', 'r') as f:
    lines = f.readlines()

  numbers = [line.strip() for line in lines]
  
  #Función que verifica si el producto está y guarda el precio
  def checkPrice(lista, producto):
    nodo_actual = lista.head
    while nodo_actual is not None:
      if producto in nodo_actual.serial:
        identificador = nodo_actual.serial
        precio = nodo_actual.data
        list_of_compare_prices.append(identificador, precio)
        # return identificador, precio
      nodo_actual = nodo_actual.next

  def comparePrices(lista):
    if lista.head is None:
      return None
    else:
      minimo = lista.head.data
      serial = lista.head.serial
      actual = lista.head.next
      while actual is not None:
        if int(actual.data) < int(minimo):
          minimo = actual.data
          serial = actual.serial
        actual = actual.next
      print(
        str("El identificador ")+ desiredProduct + str(" con valor mas bajo se encuentra en: ") + serial +
        str(" con valor: ") + minimo)

  #Se ingresa un número determinado para la cantidad de tiendas
  for item in range(10):
    desiredProduct = random.choice(numbers)
    checkPrice(list_of_data, desiredProduct)
    # productsComparison = DoubleLinkedList()
    comparePrices(list_of_compare_prices)
    list_of_compare_prices.clear()

end_time = time.time()
print("Tiempo de ejecución:", end_time - start_time, "segundos")