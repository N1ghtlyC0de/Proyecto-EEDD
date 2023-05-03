from dynamicArray import DynamicArray

if __name__ == '__main__':
  
  with open("BDD.txt", "r") as fileData:
    data = fileData.readlines()
  list_of_data=DynamicArray()
  list_of_compare=DynamicArray()
  for line in data:
    line.strip()
    olx = line.split(", ")
    list_of_data.append((olx[0],olx[1]))

  size_array=list_of_data.__len__()

  def read(arreglo, producto):
    for i in range(1, size_array):
      valor1, valor2 = arreglo[i]
      if producto in valor1:
        list_of_compare.append((valor1,valor2))
        
  def compare(arreglo):
    serial, minimo = arreglo[0]
    # serial1, minimo1= arreglo[1]
    for i in range(2, size_array2):
      serial1, minimo1 = arreglo[i]
      if minimo1 < minimo:
          minimo = minimo1
          serial = serial1
    return print(str("El identificador con valor mas bajo se encuentra en: ") + serial + str(" con valor: ") + minimo)
#Se ingresa un número determinado para la cantidad de tiendas
  productsQty = int(input('Cantidad de productos que desea buscar: '))
  for item in range(productsQty):
    desiredProduct = input('Ingrese el producto que desea comprar: ')
    read(list_of_data,desiredProduct)
      # productsComparison = DoubleLinkedList()
    size_array2=list_of_compare.__len__()
    compare(list_of_compare)
    list_of_compare=[]
    
        