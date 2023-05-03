# from linkedList import LinkedList
# from doubleLinkedList import DoubleLinkedList
from stack import Stack

if __name__ == '__main__':
  with open("BDD.txt", "r") as fileData:
    data = fileData.readlines()

  list_of_data = Stack()
  list_of_compare_prices = Stack()
  for line in data:
    line.strip()
    olx = line.split(", ")
    list_of_data.push(olx[0],olx[1])

  #Función que verifica si el producto está y guarda el precio
  def check_price(lista, producto):
    nodo_actual = lista.bottom
    while nodo_actual is not None:
      if producto in nodo_actual.serial:
        identificador = nodo_actual.serial
        precio = nodo_actual.data
        list_of_compare_prices.push(identificador, precio)
        # return identificador, precio   
      nodo_actual = nodo_actual.prev

  def compare_prices(lista):
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
  productsQty = int(input('Cantidad de productos que desea buscar: '))
  for item in range(productsQty):
    desiredProduct = input('Ingrese el producto que desea comprar: ')
  check_price(list_of_data,desiredProduct)
    # productsComparison = DoubleLinkedList()
  compare_prices(list_of_compare_prices)