from stack import Stack
import time
import random
start_time = time.time()

if __name__ == '__main__':
  with open("BDD.txt", "r") as fileData:
    data = fileData.readlines()

  list_of_data = Stack()
  list_of_compare_prices = Stack()
  list_of_serials = Stack()
  for line in data:
    line.strip()
    olx = line.split(", ")
    list_of_data.push(olx[0],olx[1])

  stack_size = list_of_data.__len__()

  with open("serials_choice.txt","r") as fileData2:
    serial_random = fileData2.readlines()
    
  for line in serial_random:
    list_of_serials.push(line.strip())
  size_of_list_of_serials=list_of_serials.__len__()
  
  #Función que verifica si el producto está y guarda el precio
  def checkPrice(lista, producto):
    nodo_actual = lista.bottom
    while nodo_actual is not None:
      if producto in nodo_actual.serial:
        identificador = nodo_actual.serial
        precio = nodo_actual.data
        list_of_compare_prices.push(identificador, precio)  
      nodo_actual = nodo_actual.prev

  def comparePrices(lista):
    if lista.bottom is None:
      return None
    else:
      minimo = lista.bottom.data
      serial= lista.bottom.serial
      actual = lista.bottom.prev
      while actual is not None:
        if actual.data < minimo:
            minimo = actual.data
            serial= actual.serial
        actual = actual.prev
      return print(str("El identificador con valor mas bajo se encuentra en: ") + serial + str(" con valor: ") + minimo)
      
  #Se ingresa un número determinado para la cantidad de tiendas
  productsQty = random.randint(1, 20)
  for item in range(productsQty):
    indice_aleatorio = random.randint(0,size_of_list_of_serials-1)
    desiredProduct = list_of_serials[indice_aleatorio]
  checkPrice(list_of_data,desiredProduct)
  comparePrices(list_of_compare_prices)

end_time = time.time()
print("Tiempo de ejecución:", end_time - start_time, "segundos")