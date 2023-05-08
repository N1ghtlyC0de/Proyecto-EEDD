from queue import Queue
import time
import random
start_time = time.time()

if __name__ == '__main__':
  with open("BDD.txt", "r") as fileData:
    data = fileData.readlines()

  list_of_data = Queue()
  list_of_compare_prices = Queue()
  list_of_serials = Queue()
  for line in data:
    line.strip()
    olx = line.split(", ")
    list_of_data.enqueue(olx[0],olx[1])

  size_of_list_of_serials = list_of_serials.__len__()

  #Función que verifica si el producto está y guarda el precio
  def checkPrice(lista, producto):
    nodo_actual = lista.front
    while nodo_actual is not None:
      if producto in nodo_actual.serial:
        identificador = nodo_actual.serial
        precio = nodo_actual.data
        list_of_compare_prices.enqueue(identificador, precio)
        # return identificador, precio   
      nodo_actual = nodo_actual.next

  def comparePrices(lista):
    if lista.front is None:
            return None
    else:
            minimo = lista.front.data
            serial= lista.front.serial
            actual = lista.front.next
            while actual is not None:
                if actual.data < minimo:
                    minimo = actual.data
                    serial= actual.serial
                actual = actual.next
            return print(str("El identificador con valor mas bajo se encuentra en: ") + serial + str(" con valor: ") + minimo)
      
  #Se ingresa un número determinado para la cantidad de tiendas
  productsQty = random.randint(1, 20)
  for item in range(productsQty):
 
  checkPrice(list_of_data,desiredProduct)
  comparePrices(list_of_compare_prices)
  list_of_compare_prices.clearQueue()

end_time = time.time()
print("Tiempo de ejecución:", end_time - start_time, "segundos")